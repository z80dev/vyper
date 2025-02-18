# pragma version ^0.4.0

owner: address

@deploy
def __init__():
    self.owner = msg.sender

# marked virtual to allow overriding with additional checks
@virtual
@external
def setOwner(newOwner: address):
    assert msg.sender == self.owner
    self.owner = newOwner
