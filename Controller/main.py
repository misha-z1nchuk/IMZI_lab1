import Model.parse_input as prs
from Model.model import dlnet
from Model.JSONEncoder import Write, Read
from View.view import View
Yh = []


def debug():
    x, y, path = prs.parse("training")
    nn = dlnet(x, y)
    nn.gd(iter=10000)
    Write(nn)


def release():
    x, y, path = prs.parse("check")

    nn = dlnet(x, y)
    Read(nn)
    Yh = nn.forward()
    Yh *= 100
    view = View(Yh, path)


info = input("\nFunctional version:\nDebug (network training) - 0\nRelease - 1\n\nYour choice :")
if info == "0":
    debug()
if info == "1":
    release()
