# Laboratorio 10
In questo laboratorio viene richiesto di sviluppare un programma più complesso
che richiede l'utilizzo di molti dei concetti discussi durante il corso.
La struttura del laboratorio segue quella di una prova d'esame.

# Diet
Sviluppare un'applicazione che consenta di gestire la dieta tramite il calcolo dei valori nutritivi.
L'applicazione deve permettere di definire le materie prime, di utilizzarle come ingredienti per delle ricette,
di gestire prodotti confezionati e menù, e registrare chef.

I moduli e le classi vanno sviluppati nel package *diet*.
Non spostare o rinominare le classi esistenti e non modificare le signature dei metodi.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Questo verrà fornito all'esame.

Nel package *tests* vengono forniti dei test simili a quelli che valutano una prova d'esame.
Questi non verranno forniti all'esame ma saranno disponibili solamente per la correzione a casa.

## R1: Materie Prime
Il sistema interagisce principalmente tramite la classe *Food*.

Viene fornita classe astratta NutritionalElement rappresentante un alimento con valori nutrizionali.
Essa definisce un'interfaccia comune (metodi e rispettive signatures) per le classi che ereditano da essa.

*NutritionalElement* definisce le properties ```name(self) -> str```,
```calories(self) -> float```,
```proteins(self) -> float```,
```carbs(self) -> float```,
```fats(self) -> float```,
```per100g(self) -> bool```,
rappresentanti rispettivamente il nome dell'alimento,
le quantità di kilo-calorie, proteine, carboidrati e grassi in esso contenuti,
e un valore booleano che esprime se queste quantità si riferiscono a una dose di 100g (*True*)
o sono i valori assoluti (*False*). 

Una materia prima (ad es., olio, zucchero, ecc...) deve implementare la classe astratta NutritionalElement.
Per essa le quantità dei valori nutrizionali sono riferiti a 100g.

Per definire una materia prima, si utilizza il metodo 
```define_raw_material(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None```
della classe *Food*.
Il metodo riceve come parametri il nome della materia prima e i valori nutrizionali riferiti a 100 grammi.
Il metodo lancia un'eccezione di tipo *ValueError* se una materia prima con lo stesso nome è già stata definita.

La property ```raw_materials(self) -> List[NutritionalElement]``` di *Food* 
restituisce la lista di materie prime in ordine alfabetico.

Il metodo ```get_raw_material(self, name: str) -> NutritionalElement``` di *Food*
restituisce la materia prima dato il nome.

**ATTENZIONE**: I type hint *NutritionalElement* e *List[NutritionalElement]*
non indicano solamente un NutritionalElement o una lista di NutritionalElement,
ma includono anche oggetti di classi che derivano da *NutritionalElement* o liste di essi.
Infatti non è possibile creare oggetti *NutritionalElement* in quanto la classe è astratta.


## R2: Prodotti
Un prodotto preconfezionato (ad esempio un cono gelato) deve implementare la classe astratta NutritionalElement.
Per esso i valori nutrizionali sono espressi per il prodotto intero e **NON** su 100 grammi.
La property ```per100g(self) -> bool``` deve pertanto restituire *False*.

I prodotti vengono definiti tramite il metodo
```define_product(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None```
della classe *Food*.
Il metodo riceve come parametri il nome e i valori nutrizionali complessivi per il prodotto (ovvero **NON** per 100 g).
Il metodo lancia un'eccezione di tipo *ValueError* se un prodotto con lo stesso nome è già stato definito.

La property ```products(self) -> List[NutritionalElement]``` di *Food*
restituisce la lista dei prodotti in ordine alfabetico

Il metodo ```get_product(self, name: str) -> NutritionalElement``` di *Food*
restituisce il prodotto dato il nome.


## R3: Ricette
Le materie prime possono essere combinate come ingredienti di ricette.
Le ricette sono rappresentate da oggetti di classe *Recipe*, che eredita da *NutritionalElement*.

Per definire una ricetta viene utilizzato il metodo ```create_recipe(self, name: str) -> Recipe```,
che riceve come parametro il nome della ricetta, che può essere considerato unico (**NON** controllarlo).
Il metodo restituisce la ricetta creata.

È possibile aggiungere ingredienti alle ricette tramite il metodo
```add_ingredient(self, raw_material_name: str, quantity: float) -> "Recipe"```,
che riceve come parametri il nome di una materia prima e la sua quantità in grammi.
Esso restituisce un riferimento alla ricetta su cui è chiamato (*self*).

La property ```recipes(self) -> List[Recipe]``` di *Food*
restituisce la lista delle ricette che sono state definite.

Il metodo ```get_recipe(self, name: str) -> Recipe``` di *Food*
restituisce la ricetta dato il nome.

I valori nutrizionali di una ricetta vanno calcolati 
in base a quelli degli ingredienti che la compongono e alle loro quantità.
Essi vanno espressi su 100g (**ATTENZIONE** a come calcolarli).

Il metodo
```calculate_nutritional_value(self, get_nutritional_value: Callable[[NutritionalElement], float]) -> float```
di *Recipe* riceve come parametro una funzione lambda.
La funzione lambda riceve come parametro un *NutritionalElement* e restituisce uno dei suoi valori nutrizionali.
Il metodo deve restituire il valore nutrizionale della ricetta, espresso su 100g,
usando i valori nutrizionali estratti dai sui ingredienti tramite la lambda, e pensandoli secondo le quantità.

Il metodo ```__repr__(self) -> str``` di *Recipe*
restituisce una stringa contenente le informazioni di ciascun ingrediente che la compone.
Per ogni ingrediente indicare nome e quantità (espressa su una cifra decimale), separandoli con uno spazio.
Le informazioni di ciascun ingrediente devono essere separate da un carattere di a capo (*\n*). Esempio:
```
Pasta 70.0
Passata di Pomodoro 30.0
Olio di oliva 5.0
```

**SUGGERIMENTO:** può essere comodo passare al costruttore di *Recipe* un riferimento all'oggetto *Food* che la crea,
di modo che dalle istanze di *Recipe* sia possibile accedere agli oggetti prodotto e materia prima
tramite i metodi di *Food*.

**SUGGERIMENTO:** Il metodo ```calculate_nutritional_value``` può essere opportunamente riutilizzato
per l'implementazione delle properties che restituiscono i valori nutrizionali.


## R4: Menù
Il menù è composto sia da porzioni di ricette sia da prodotti preconfezionati.
I menù sono rappresentate da oggetti di classe *Menu*, che eredita da *NutritionalElement*.

Un nuovo menù è creato tramite il metodo ```create_menu(self, name: str) -> Menu``` della classe *Food*
Il metodo accetta come parametro il nome (unico, ma **NON** controllarlo) del menù
e restituisce il *Menu* creato.

È possibile aggiungere una porzione di una ricetta a un Menù tramite il metodo
```add_recipe(self, recipe_name: str, quantity: float) -> "Menu"```
che riceve come parametro il nome di una ricetta e la dimensione della porzione in grammi.
Esso restituisce un riferimento all menù su cui è chiamato (*self*).

Per aggiungere un prodotto preconfezionato,
la classe Menu offre il metodo ```add_product(self, product_name: str) -> "Menu"```
che riceve come parametro il nome del prodotto.

I valori nutrizionali di un menù vanno calcolati 
in base a quelli dei prodotti e delle ricette che lo compongono e alle loro quantità.
I valori nutrizionali vanno espressi in modo assoluti e **NON** riferiti a 100g (**ATTENZIONE** a come calcolarli).

**SUGGERIMENTO** come per *Recipe*, 
può essere comodo passare al costruttore di *Menu* un riferimento all'oggetto *Food* che lo crea,
di modo che dalle istanze di *Menu* sia possibile accedere agli oggetti prodotto e materia prima
tramite i metodi di *Food*.


## R5: Chef
Uno chef è identificato univocamente dal suo nome.
Il metodo ```add_chef(self, chef_name: str, fav_recipe: str, recipes: Optional[List[str]] = None) -> None```
di *Food* permette di aggiungere uno chef dato il suo nome, il nome della sua ricetta preferita,
e un lista di nomi di ricette da lui ideate.

Il metodo ```chef_recognition(self, chef_name: str) -> List[str]``` di *Food* riceve come parametro il nome di uno chef,
e restituisce una lista di nomi di chef. Ogni chef ha una ricetta preferita, che sarà stata ideata da un altro chef,
che a sua volta avrà una ricetta preferita ideata da una altro chef ancora e così via.
La lista restituita deve pertanto contenere i nomi degli chef seguendo la catena di preferenze,
partendo da quello fornito come parametro e terminante in uno chef che ha come ricetta preferita una dello chef di partenza.
Nel caso in cui non si possa raggiungere lo chef di partenza seguendo la catena delle preferenze, restituire una lista vuota.

Considerare il caso in cui ogni chef abbia sempre una ricetta preferita,
e che ogni ricetta preferita abbia sempre uno chef ideatore.

**SUGGERIMENTO**: il problema in questione è l'esplorazione di un grafo in cui i nodi sono gli chef
e le connessioni avvengono attraverso le ricette.
La ricerca ha successo quando uno dei nodi già visitati, adiacente a quello preso in considerazione, è il nodo di partenza.



