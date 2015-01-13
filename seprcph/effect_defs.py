from seprcph.effect import Effect
from seprcph.train import Train

def do_faster(train):
    train.speed *= 2

def undo_faster(train):
    train.speed /= 2

eff_faster = Effect("Faster", Train, do_faster, undo_faster, 3)
