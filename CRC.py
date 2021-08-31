import tkinter as tk
import re

labelWidget = None
textWidget = None
labelMulWidget = None
textMulWidget = None
button = None
labelEncodeRes = None
labelDecodeRes = None


def XOR(str1, str2):  # 实现模2减法
    ans = ''
    if str1[0] == '0':
        return '0', str1[1:]
    else:
        for i in range(len(str1)):
            if (str1[i] == '0' and str2[i] == '0'):
                ans = ans + '0'
            elif (str1[i] == '1' and str2[i] == '1'):
                ans = ans + '0'
            else:
                ans = ans + '1'
    return '1', ans[1:]


def CRC_Encoding(str1, str2):  # CRC编码
    if str2[0] == '0':
        return "多项式首位不能为0"
    if str2[-1] == '0':
        return "多项式最后一位不能为0"
    if len(str1) == 0 or len(str2) == 0:
        return "Input Empty!"
    string = "!@#$%^&~*()_+=-23456789"
    for i in string:
        if i in str1 + str2:
            return "Input Error" + "  " + i
    strmatch = re.compile(r'[A-Za-z]', re.S)
    res = re.findall(strmatch, str1 + str2)
    if len(res):
        return "Input Error" + "  " + str(res)
    lenght = len(str2)
    str3 = str1 + '0' * (lenght - 1)
    ans = ''
    yus = str3[0:lenght]
    for i in range(len(str1)):
        str4, yus = XOR(yus, str2)
        ans = ans + str4
        if i == len(str1) - 1:
            break
        else:
            yus = yus + str3[i + lenght]
    ans = str1 + yus
    return ans


def CRC_Decoding(str1, str2):  # CRC解码
    if str2[0] == '0':
        return "多项式首位不能为0"
    if str2[-1] == '0':
        return "多项式最后一位不能为0"
    if len(str1) == 0 or len(str2) == 0:
        return "Input Empty!"
    string = "!@#$%^&~*()_+=-23456789"
    for i in string:
        if i in str1 + str2:
            return "Input Error" + "  " + i
    strmatch = re.compile(r'[A-Za-z]', re.S)
    res = re.findall(strmatch, str1 + str2)
    if len(res):
        return "Input Error" + " " + str(res)
    lenght = len(str2)
    str3 = str1 + '0' * (lenght - 1)
    ans = ''
    yus = str3[0:lenght]
    for i in range(len(str1)):
        str4, yus = XOR(yus, str2)
        ans = ans + str4
        if i == len(str1) - 1:
            break
        else:
            yus = yus + str3[i + lenght]
    if yus == '0' * len(yus):
        return str1[0:len(str1) - len(str2)+1]
    else:
        return "Information Error"


def executeEncode():
    global textWidget
    global textMulWidget
    global labelEncodeRes
    # content1 = textWidget.get("0.0", "end")
    # content2 = textMulWidget.get("0.0", "end")
    if labelEncodeRes is not None:
        labelEncodeRes.pack_forget()
    resultEncode = CRC_Encoding(textWidget.get("0.0", "end")[:-1], textMulWidget.get("0.0", "end")[:-1])
    labelEncodeRes = tk.Label(master=window, text=resultEncode, width=20, height=1)
    labelEncodeRes.pack()


def executeDecode():
    global textWidget
    global textMulWidget
    global labelDecodeRes
    # content1 = textWidget.get("0.0", "end")
    # content2 = textMulWidget.get("0.0", "end")
    if labelDecodeRes is not None:
        labelDecodeRes.pack_forget()
    resultDecode = CRC_Decoding(textWidget.get("0.0", "end")[:-1], textMulWidget.get("0.0", "end")[:-1])
    labelDecodeRes = tk.Label(master=window, text=resultDecode, height=1)
    labelDecodeRes.pack()


def showInfo():
    global labelMulWidget
    global labelWidget
    global textMulWidget
    global textWidget
    global button
    global labelDecodeRes
    global labelEncodeRes
    choice = var.get()
    label1.config(text="You have choosed " + choice)
    if labelWidget is not None:
        labelMulWidget.pack_forget()
        labelWidget.pack_forget()
        textMulWidget.pack_forget()
        textWidget.pack_forget()
        button.pack_forget()
        if labelEncodeRes is not None:
            labelEncodeRes.pack_forget()
        if labelDecodeRes is not None:
            labelDecodeRes.pack_forget()

    if choice == "CRC encode":
        labelWidget = tk.Label(master=window, height=1, text="请输入需要编码的内容")
        labelWidget.pack()
        textWidget = tk.Text(master=window, height=1, width=20)
        textWidget.pack()
        labelMulWidget = tk.Label(master=window, height=1, text="请输入生成多项式")
        labelMulWidget.pack()
        textMulWidget = tk.Text(master=window, height=1, width=20)
        textMulWidget.pack()
        button = tk.Button(master=window, text="Encode", width=20, height=1, command=executeEncode)
        button.pack()
    elif choice == "CRC decode":
        labelWidget = tk.Label(master=window, height=1, text="请输入需要解码的内容")
        labelWidget.pack()
        textWidget = tk.Text(master=window, height=1, width=20)
        textWidget.pack()
        labelMulWidget = tk.Label(master=window, height=1, text="请输入生成多项式")
        labelMulWidget.pack()
        textMulWidget = tk.Text(master=window, height=1, width=20)
        textMulWidget.pack()
        button = tk.Button(master=window, text="Decode", width=20, height=1, command=executeDecode)
        button.pack()


if __name__ == '__main__':
    # 创建一个窗口
    window = tk.Tk()
    window.title("CRC编码与解码")
    window.geometry('300x400')

    var = tk.StringVar()
    label1 = tk.Label(master=window, bg='yellow', height=1, text='empty')
    label1.pack()
    rEncode = tk.Radiobutton(master=window, text='CRC Encode', variable=var, value='CRC encode', command=showInfo)
    rEncode.pack()
    rDecode = tk.Radiobutton(master=window, text='CRC Decode', variable=var, value='CRC decode', command=showInfo)
    rDecode.pack()

    window.mainloop()
