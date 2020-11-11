from PIL import Image

def convert(data):
    l=[]
    for i in data:
        l.append(format(ord(i),'08b'))
    return l

def modifier(pix,data):
    dataset=convert(data)
    ld= len(dataset)
    idata= iter(pix)

    for i in range(ld):
        pix=[value for value in idata.__next__()[:3]+idata.__next__()[:3]+idata.__next__()[:3]]

        for j in range(8):
            if dataset[i][j]=="1" and pix[j]%2==0:
                pix[j]+=1
            elif dataset[i][j]=="0" and pix[j]%2!=0:
                pix[j]+=1
        if i!=ld-1 and pix[-1]%2!=0:
            pix[-1]+=1
        if i==ld-1 and pix[-1]%2==0:
            pix[-1]+=1
        pix=tuple(pix)
        yield pix[:3]
        yield pix[3:6]
        yield pix[6:9]
            
def ec(im,data):
    w=im.size[0]
    x,y=0,0
    for pixel in modifier(im.getdata(),data):
        im.putpixel((x,y),pixel)
        if x==w-1:
            x=0
            y+=1
        else:
            x+=1
    

def encode():
    img=input('Enter image name with extension:\n')
    image=Image.open(img,'r')
    data=input('Enter message you wish to encode:\n')
    if len(data)==0:
        raise ValueError('No data entered')
    im= image.copy()
    ec(im,data)
    The_choosen_name= input('Tell me the name of my new creation(without extension): \n')
    im.save(The_choosen_name+'.png')
    print("Yooo Hooo.... task completed")

def decode(img):
    output=""
    image=Image.open(img,'r')
    idata=iter(image.getdata())
    while True:
        b_str=""
        pix=[value for value in idata.__next__()[:3]+idata.__next__()[:3]+idata.__next__()[:3]]
        for i in range(8):
            if pix[i]%2==0:
                b_str+='0'
            else:
                b_str+='1'

        output+=chr(int(b_str,2))

        if pix[-1]%2==1:
            return output
    
    




a=int(input('Enter 1 to encode your message\nOr\nEnter 2 to decode your message:\n'))
if a==1:
    encode()
elif a==2:
    img=input('Enter image name with extension:\n')
    print('Your secret message is: '+ decode(img))
    print('Ssssshhhhhhh.... keep it a secret')
else:
    raise ValueError('Please provide correct input')
