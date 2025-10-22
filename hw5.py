frontend = {"krishna","Ansi" ,"Anvi","Aishu","Alna"}
backend = {"Aishu","Alna","Misa"}
backend.add("Megha")
#print(backend)
frontend.remove("Anvi")
#print(frontend)
print("students in both frontend and backend courses:",frontend & backend)
print("students only in backend not in frontend:",backend - frontend)
print("total number of unique students:",len(frontend.union(backend)))
students = {
    "frontend": len(frontend),
    "backend" : len(backend)
}
for x,y in students.items():
    print(f"course:{x},count:{y}")

fullstack = {**students, "fullstack": students["frontend"] + students["backend"]}
print("Updated course dictionary with Fullstack:",fullstack)
