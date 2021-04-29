# Design Documents: Location

## View: melbourne

### Map
```
function (doc) {
  var loc = doc.user.location.toLowerCase()
  if (loc.includes('melbourne')) {
    emit(doc, 1);
  }
} 
```

### Reduce
None

## View: sydney

### Map
```
function (doc) {
  var loc = doc.user.location.toLowerCase()
  if (loc.includes('sydney')) {
    emit(doc, 1);
  }
} 
```

### Reduce
None

## View: perth

### Map
```
function (doc) {
  var loc = doc.user.location.toLowerCase()
  if (loc.includes('perth')) {
    emit(doc, 1);
  }
} 
```

### Reduce
None
