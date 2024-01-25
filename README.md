# Rooser take-home Python tech test

## How to run

```shell
cd wordpuzzle
python manage.py runserver
```

## Example GET request sent over the API 

```
startWord: oyster
endWord: mussel

http://127.0.0.1:8000/api/wordpuzzle?startWord=oyster&endWord=mussel
```

## Testing 

```
python3 manage.py test
```

Should yield: 

```
----------------------------------------------------------------------
Ran 12 tests in 2.953s

OK
```



