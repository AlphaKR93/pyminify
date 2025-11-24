from fastapi import FastAPI
A=FastAPI()
@A.get('/')
async def B():return{'message':'Hello, world!'}
app=A