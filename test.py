import pybase64

with open(r"sample.png","rb") as f:
    z=f.read()
    # print(z)
    
img = pybase64.b64encode(z)
print(img)

def fun (hello):
    print(hello)