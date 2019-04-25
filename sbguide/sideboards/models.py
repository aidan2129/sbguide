from django.db import models

# Create your models here.
class Sideboard(models.Model):
    """
        Matchup between two decks
    """
    deck = models.ForeignKey('decks.deck', related_name='sideboard_deck', on_delete=models.CASCADE)
    opponent = models.ForeignKey('decks.deck', related_name='opponent_deck', on_delete=models.CASCADE)

    def __str__(self):
        return  "%s v %s" % (self.deck.deck_name, self.opponent.deck_name)

    def __unicode__(self):
        return  "%s v %s" % (self.deck.deck_name, self.opponent.deck_name)

    def get_sb_items(self):
        return SideboardItem.objects.filter(sideboard=self)
    
    def get_cards_in(self):
        return [{'qty': d.delta, 'card' :d.card.name} for d in self.get_sb_items() if d.delta > 0]
    
    def get_cards_out(self):
        return [{'qty': abs(d.delta), 'card' :d.card.name} for d in self.get_sb_items() if d.delta < 0]
    
    def check_sanity(self):
        diff = sum([sideboarditem.delta for sideboarditem in self.get_sb_items()])
        if diff == 0:
            return True
        return False

class SideboardItem(models.Model):
    """
        Cards coming in or out represented by positive or negative integer field 2 or -2
    """
    sideboard = models.ForeignKey('sideboards.sideboard', related_name='sideboarditem_sideboard', on_delete=models.CASCADE)
    card = models.ForeignKey('cards.card', related_name='sideboarditem_card', on_delete=models.CASCADE)
    delta = models.IntegerField()

    def in_or_out(self):
        if self.delta > 0:
            return "%s in" % self.delta
        elif self.delta < 0:
            return "%s out" % self.delta
    def __str__(self):
        return  "%s  %s" % (self.card.name, self.in_or_out())

    def __unicode__(self):
        return  "%s  %s" % (self.card.name, self.in_or_out())