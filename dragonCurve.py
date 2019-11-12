#利用turtle绘制龙形分形曲线 (Dragon Curve)
import turtle

#递归调用函数产生字符串绘图序列
def dragonCurveInit(resString, n):
    #f表示向前移动， x、y用于标记，+、-分别表示左旋、右旋90°
    store = {'x':'x+yf', 'y':'fx-y', 'f':'f', '-':'-', '+':'+'}
    resString = ''.join([store[i] for i in resString])
    if n > 1: return dragonCurveInit(resString, n-1)
    else: return resString

#绘制长度为size的龙形曲线
def dragonCurvePlot(size):
    curve = dragonCurveInit('fx', size)
    for i in curve:
        if i == 'f': turtle.forward(4)
        elif i == '+': turtle.right(90)
        elif i == '-': turtle.left(90)

def main():
    n = int(input("请输入需要得到的龙形曲线的长度: "))
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    dragonCurvePlot(n)

if __name__ == "__main__" :
    main()