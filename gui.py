import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
# window = sg.Window('My To-Do App', layout=[[label,input_box]]) # [label,input_box]가 같은 row에 있음
window = sg.Window('My To-Do App', layout=[[label],[input_box, add_button]]) # label과 input_box가 다른 row에 있음
window.read()
print("Hello")
window.close()