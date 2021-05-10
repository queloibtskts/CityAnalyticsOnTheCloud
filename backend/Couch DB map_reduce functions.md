# Design Documents: Location
## View: countTweetByStates
curl -XGET "http://\<username>:\<password>@\<hostIP>:5984/\<dbName>/_design/\<designDocumentName>/_view/countTweetByStates?group=true"

e.g. curl -XGET "http://admin:12354@localhost:5984/ccc_twitter_test5/_design/location/_view/countTweetByStates?group=true"
### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  var loc2 = doc.user.location.toLowerCase();
  var allLoc = ['victoria', 'act', 'new south wales', 'northern territory', 'queensland', 'tasmania', 'western australia', 'south australia'];
  for (var i=0; i < allLoc.length; i++) {
      if (loc.includes(allLoc[i]) || loc2.includes(allLoc[i])) {
          emit(allLoc[i], 1);
      }
  }
}
```
### Reduce
_count


## View: victoria

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('victoria')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('victoria')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None

## View: newsouthwales

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('new south wales')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('new south wales')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None


## View: southaustralia

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('south australia')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('south australia')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None

## View: queensland

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('queensland')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('queensland')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None

## View: westernaustralia

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('western australia')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('western australia')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None

## View: tasmania

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('tasmania')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('tasmania')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None


## View: act

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('act')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('act')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None


## View: northernterritory

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('northern territory')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('northern territory')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None

## View: jervisbayterritory

### Map
```
function (doc) {
  var loc = doc.place.full_name.toLowerCase();
  if (loc.includes('jervis bay territory')) {
    emit(doc, 1);
  } else {
    var loc2 = doc.user.location.toLowerCase();
    if (loc2.includes('jervis bay territory')) {
      emit(doc, 1);
    }
  }
}
```

### Reduce
None


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
