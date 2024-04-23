from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import database as db

app = FastAPI()

# uvicorn main:app --reload

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()


    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    intent_handler_dict = {
        'mid1.result - next': handle_mid1,
        'mid2.result - next': handle_mid2,
        'semester.result - next': sem_result,
        'syb - next': syb_subName
    }

    return intent_handler_dict[intent](parameters)

def syb_subName(parameters:dict):

    sem = parameters['number'][0]

    if sem in range(1,5):
        sem1 = str(sem)

        ls = []

        for i in range(1,6):
            # print(i)
            res = db.syb_sub(sem, i)
            ls.append(res)


        return JSONResponse(content={
            "fulfillmentText": f"Here is your {int(sem)} semester subjects: \n"
                               f"{', '.join(ls)}"

        })

    return JSONResponse(content={
        "fulfillmentText": f"Please enter the semester number in range of 1-4"
    })
def handle_mid1(parameters:dict):

    roll_no = parameters["roll_number"][0]
    ls_sub = ['subject1_marks', 'subject2_marks', 'subject3_marks', 'subject4_marks', 'subject5_marks', 'subject1_id',
              'subject2_id', 'subject3_id', 'subject4_id', 'subject5_id']

    name = db.check_stuID(roll_no)
    # print(name)
    if name:

        exam = 'mid1results'

        ls = []
        for sub in ls_sub:
            val = db.get_stu_mid1result(roll_no, sub, exam)
            ls.append(val)
        ls_first = ls[:4]
        ls_last = ls[5:]
        ls2 = []
        for sub_id in ls_last:
            val = db.get_stu_subName(sub_id)
            ls2.append(val)
        res = dict(zip(ls2, ls))
        # print(res)

        return JSONResponse(content={
            "fulfillmentText": f"Here is your Mid 1 result: "\
                               f"Student name: {name}"
                               f"{res}"

        })

    elif name is None:
        return JSONResponse(content={
            "fulfillmentText": f"Student not found with student Id: {roll_no}"

        })

def handle_mid2(parameters:dict):

    roll_no = parameters["roll_number"][0]
    # print(roll_no)
    ls_sub = ['subject1_marks', 'subject2_marks', 'subject3_marks', 'subject4_marks', 'subject5_marks', 'subject1_id',
              'subject2_id', 'subject3_id', 'subject4_id', 'subject5_id']

    name = db.check_stuID(roll_no)
    # print(name)
    if name:

        exam = 'mid2results'

        ls = []
        for sub in ls_sub:
            val = db.get_stu_mid1result(roll_no, sub, exam)
            ls.append(val)
        ls_first = ls[:4]
        ls_last = ls[5:]
        ls2 = []
        for sub_id in ls_last:
            val = db.get_stu_subName(sub_id)
            ls2.append(val)
        res = dict(zip(ls2, ls))
        # print(res)

        return JSONResponse(content={
            "fulfillmentText": f"Here is your Mid 2 result: "\
                               f"Student name: {name}"
                               f"{res}"

        })

    elif name is None:
        return JSONResponse(content={
            "fulfillmentText": f"Student not found with student Id: {roll_no}"

        })

def sem_result(parameters:dict):

    roll_no = parameters["roll_number"][0]
    ls_sub = ['subject1_marks', 'subject2_marks', 'subject3_marks', 'subject4_marks', 'subject5_marks', 'subject1_id',
              'subject2_id', 'subject3_id', 'subject4_id', 'subject5_id', 'status']

    name = db.check_stuID(roll_no)
    # print(name)
    if name:
        exam = 'semesterresults'

        ls = []
        for sub in ls_sub:
            val = db.get_stu_mid1result(roll_no, sub, exam)
            ls.append(val)
        ls_first = ls[:4]
        ls_last = ls[5:10]
        state = ls[-1]
        ls2 = []
        for sub_id in ls_last:
            val = db.get_stu_subName(sub_id)
            ls2.append(val)
        res = dict(zip(ls2, ls))
        # print(res)

        return JSONResponse(content={
            "fulfillmentText": f"Here is your Sem result: \n"
                               f"Student name: {name} \n"
                               f"{res}\n"
                               f"Status: {state}"

        })

    elif name is None:
        return JSONResponse(content={
            "fulfillmentText": f"Student not found with student Id: {roll_no}"

        })


@app.get("/")
async def root():
    return {"message": "Hello World"}