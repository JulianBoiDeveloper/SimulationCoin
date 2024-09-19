class CarteBancaire:
    def __init__(self, titulaire,numero, expiration, cvv,somme=100000):
        self.titulaire = titulaire
        self.numero = numero
        self.expiration = expiration
        self.cvv = cvv
        self.somme = somme
    def __str__(self):
        return f"CarteBancaire = ( Titulaire =>{self.titulaire} / {self.somme} €, Numéro de carte => {self.numero}, Date d'expération => {self.expiration}, CVV => {self.cvv})"
