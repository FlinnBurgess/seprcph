from seprcph.effect import Effect
from seprcph.train import Train
from seprcph.player import Player


def pass_function():
    """ 
    Do nothing
    """
    pass


def double_speed(train):
    """
    Doubles the train's speed
    
    Args:
        train: The train to be affected
    """
    train.speed *= 2


def half_speed(train):
    """
    Halves the train's speed
    
    Args:
        train: The train to be affected
    """
    train.speed /= 2


def reduce_load(train):
    """ 
    Reduces the train's load by 100
    
    Args:
        train: The train to be affected
    """
    train.current_load -= 100
    if train.current_load < 0:
        train.current_load = 0


def do_investor(player):
    """
    Increases the player's gold by 5
    
    Args:
        player: The player to be affected
    """
    player.gold += 5

eff_faster = Effect("Faster", Train, double_speed, half_speed, 3)
eff_slower = Effect("Slower", Train, half_speed, double_speed, 3)
eff_train_robbery = Effect("Robbery", Train, reduce_load, pass_function, 1)
eff_investor = Effect("Investor", Player, do_investor, pass_function, 1)
