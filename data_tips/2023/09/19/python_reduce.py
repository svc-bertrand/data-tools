from functools import reduce


def example_01():
    # Concaténer tous les caractères d’une liste

    carac = ["d", "a", "t", "a"]

    def concat_all(x, y):
        return x + y

    text = reduce(concat_all, carac)

    print("************************************ Résultat de l'exemple 1 **********************************************")
    print(text)
    # Résultat : data

def example_02():
    text = "Data Engineering"

    def double_carac(x, y):
        return x + y * 2

    new_text = reduce(double_carac, text, "")

    print("************************************ Résultat de l'exemple 2 **********************************************")
    print(new_text)
    # Résultat : DDaattaa  EEnnggiinneeeerriinngg

def example_03():
    list = [1, 2, 3, 4]

    def sum_all(x, y):
        return x + y ** 2

    final = reduce(sum_all, list, 0)

    print("************************************ Résultat de l'exemple 3 **********************************************")
    print(str(final))
    # Résultat : 30

def example_04():
    # Liste des transactions
    transactions = [
        {'product_id': 1, 'amount': 100.5},
        {'product_id': 2, 'amount': 50.0},
        {'product_id': 1, 'amount': 200.5},
        {'product_id': 3, 'amount': 30.0},
        {'product_id': 2, 'amount': 60.0},
        {'product_id': 3, 'amount': 30.0},
    ]

    def aggregate_sales(total_sales, transaction):
        product_id = transaction['product_id']
        amount = transaction['amount']

        # Si le produit existe déjà dans le total, on ajoute le montant de
        # la transaction à son total.
        # Sinon, on crée une nouvelle entrée pour ce produit avec le
        # montant de la transaction.
        if product_id in total_sales:
            total_sales[product_id] += amount
        else:
            total_sales[product_id] = amount

        return total_sales

    # Utilisation de reduce pour obtenir le total des ventes par produit.
    # Il est nécessaire de lui fournir une valeur initiale qui est {}
    total_sales_per_product = reduce(aggregate_sales, transactions, {})

    print("************************************ Résultat de l'exemple 4 **********************************************")
    print(total_sales_per_product)
    # Résultat : {1: 301.0, 2: 110.0, 3: 60.0}


example_01()
example_02()
example_03()
example_04()