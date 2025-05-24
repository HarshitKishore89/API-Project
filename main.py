

from fastapi import FastAPI, Path,HTTPException,Query
import json

app = FastAPI()
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

        return data
@app.get("/")
def hello():
    return {"message": "patient Management Syatem API"}

@app.get("/about")
def about():
    return {'message':'Fully fuctional API to manage  your patient records.'}




@app.get("/view")
def view():
    data = load_data()

    return data

@app .get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="id of the patient in the DB",example = 'P001')):
    # load all the patient

    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="patient not found")

@app.get("/sort")
def sort_patient(sort_by: str = Query(...,description='sort on the basis of height ,weight or bmi'),order:str=Query('asc',description='sort in asc or desc order')):
   valid_feilds=['height','weight','bmi']

   if sort_by not in valid_feilds:
       raise HTTPException(status_code=400, detail='invalid field select from{valid_feilds}')

   if order not in ['asc','desc']:
       raise HTTPException(status_code=400, detail='invalid order select from between asc and dsc' )

   data = load_data()

   sort_order = True if  order =='desc' else False

   sorted_data = sorted(data.values(), key=lambda x: x.get( sort_by, 0),reverse=sort_order)

   return sorted_data