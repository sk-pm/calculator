'''
calculator to calculate numeric operations and expression
Add(+)
Difference(-)
divide(/)
multiply(*).
Author:Shaik Peeramohidin
GitHub:https://github.com/sk-pm
'''
#importing  streamlit
import streamlit as st
#title to app
st.title("Calculator")
#taking inputs
var1 = st.number_input("Enter first value:")
operation = st.radio("Please select one of the following operations:",("+","-","/","*"))
var2 = st.number_input("Enter second value:")
def ADD(a,b):
    return a+b
def SUB(a,b):
    return a-b
def DIV(a,b):
    return a/b
def MUL(a,b):
    return a*b
try:
    if( st.button("Result")):
        if operation == "+":
            result = ADD(var1,var2)
            st.success("Result of {} + {} = {} ".format(var1,var2,result))
        elif operation == "-":
            result = SUB(var1,var2)
            st.success("Result of {} - {} = {} ".format(var1,var2,result))
        elif operation == "/":
            result = DIV(var1,var2)
            st.success("Result of {} / {} = {} ".format(var1,var2,result))
        elif operation == "*":
            result = MUL(var1,var2)
            st.success("Result of {} * {} = {} ".format(var1,var2,result))

except:
    st.text("Above fields can not be blank")
