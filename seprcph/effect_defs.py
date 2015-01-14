from seprcph.effect import Effect
from seprcph.train import Train
from seprcph.player import Player
from seprcph.track import Track

def pass_function():
    pass

def double_speed(train):
    train.speed *= 2

def half_speed(train):
    train.speed /= 2

def reduce_load(train):
    train.current_load -= 100
    if train.current_load < 0:
        train.current_load = 0

def do_investor(player):
    player.gold += 5

def do_broken_track(track):
    track.is_broken = True
    track.image.fill((0, 0, 0))

def undo_broken_track(track):
    track.is_broken = False
    if track.owner.player_id == 1:
        track.image.fill((0, 0, 255))
    else:
        track.image.fill((255, 0, 0))

def do_undo_hijack_track(track):
    if track.owner.player_id == 1:
        track.owner.player_id = 2
        track.image.fill((255, 0, 0))
        # This would technically work but have catastrophic effects with
        # anything that uses a player's ID, we need an alternative.
    else:
        track.owner.player_id = 1
        track.image.fill((0, 0, 255))

#def do_undo_stop_train(train):
#    if train.speed > 0:
#        old_speed = train.speed
#        train.speed = 0
#    else:
#        train.speed = old_speed

eff_faster = Effect("Faster", Train, double_speed, half_speed, 3)
eff_slower = Effect("Slower", Train, half_speed, double_speed, 3)
eff_train_robbery = Effect("Robbery", Train, reduce_load, pass_function, 1)
eff_investor = Effect("Investor", Player, do_investor, pass_function, 1)
eff_broken_track = Effect("Broken Track", Track, do_broken_track, undo_broken_track, 3)
eff_hijack_track = Effect("Hijack Track", Track, do_undo_hijack_track, do_undo_hijack_track, 1)