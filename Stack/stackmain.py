from stack import Stack
st = Stack()
ch=0
while(1):
    print("1 Push")
    print("2 Pop")
    print("3 Peep")
    print("4 Display")
    print("5 Exit")
    ch = int(input("Enter the choice :"))
    if(ch==1):
        num=int(input("Enter the Number:"))
        st.push(num)
    elif(ch==2):
        num=st.pop()
        if(num==-1):
            print("Stack is Empty")
        else:
            print('Pooped number is:',num)
    elif(ch==3):
        print("Top Element",st.peep())
    elif(ch==4):
        print(st.display())
    else:
        break;
