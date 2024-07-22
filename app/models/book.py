from odmantic import Model

class BookModel(Model):
	keyword: str
	publisher: str
	price: str 
	img: str 

	model_config = {
        "collection": "books"
    }
