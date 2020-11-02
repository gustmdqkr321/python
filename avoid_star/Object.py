class Object():
    def __init__(self):
        pass

    def playerHasHitStar(playerRect, star):
        for b in star:
            if playerRect.colliderect(b['rect']):
                star.remove(b)
                return True
        return False

    def playerHasHitHeart(playerRect, heart):
        for b in heart:
            if playerRect.colliderect(b['rect']):
                heart.remove(b)
                return True
        return False