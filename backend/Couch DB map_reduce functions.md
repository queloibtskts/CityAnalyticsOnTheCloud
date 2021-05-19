# Design Documents: Language

curl -XGET "http://\<username>:\<password>@\<hostIP>:5984/\<dbName>/_design/\<designDocumentName>/_view/\<viewName>?group=true"

e.g. $ curl -XGET "http://admin:12354@localhost:5984/vulgar_tweet_by_search/_design/language/_view/vulgarWordFreq?group=true"

## View: countTweetByStates

This MapReduce function counts the tweets from each state.

### Map
```
function (doc) {
  if (doc.place && doc.place.full_name) {
      var loc_l = doc.place.full_name.toLowerCase();
      var loc = doc.place.full_name;
  }
  if (doc.user && doc.user.location) {
      var loc2_l = doc.user.location.toLowerCase();
      var loc2 = doc.user.location;
  }
  var stateNotFound = true;
  var allLoc = ['victoria', 'act', 'new south wales', 'northern territory', 'queensland', 'tasmania', 'western australia', 'south australia'];
  var abbres = {'VIC': 'victoria', 'NSW': 'new south wales', 'NT': 'northern territory', 'QLD': 'queensland', 'TAS': 'tasmania', 'WA': 'western australia', 'SA': 'south australia'};
  for (var i=0; i < allLoc.length; i++) {
      if ( ( loc_l && loc_l.includes(allLoc[i]) ) || ( loc2_l && loc2_l.includes(allLoc[i]) ) ) {
          // var thisLoc = allLoc[i];
          stateNotFound = false;
          emit(allLoc[i], 1);
      }
  }
  if (stateNotFound) {
      for (var abbre in abbres) {
          if  ( ( loc && loc.includes(abbre) ) || ( loc2 && loc2.includes(abbre) ) ) {
              // var thisLoc = abbres[abbre];
              emit(abbres[abbre], 1);
          }
      }
  }
  // console.log(thisLoc);
}
```
### Reduce
_count


## View: vulgarWordFreq

This MapReduce function returns vulgar word frequencies in each state.

### Map
```
function (doc) {
  if (doc.place && doc.place.full_name) {
      var loc_l = doc.place.full_name.toLowerCase();
      var loc = doc.place.full_name;
  }
  if (doc.user && doc.user.location) {
      var loc2_l = doc.user.location.toLowerCase();
      var loc2 = doc.user.location;
  }
  var stateNotFound = true;
  var abbres = {'act': 'ACT', 'victoria': 'VIC', 'new south wales': 'NSW', 'northern territory': 'NT', 'queensland': 'QLD', 'tasmania': 'TAS', 'western australia': 'WA', 'south australia': 'SA'};
  var thisLoc = null;
  for (var abbre in abbres) {
      if  ( ( loc_l && loc_l.includes(abbre) ) || ( loc2_l && loc2_l.includes(abbre) ) ) {
          thisLoc = abbres[abbre];
          stateNotFound = false;
      }
  }
  if (stateNotFound) {
      for (var abbre1 in abbres) {
          if  ( ( loc && loc.includes(abbres[abbre1]) ) || ( loc2 && loc2.includes(abbres[abbre1]) ) ) {
              thisLoc = abbres[abbre1];
              stateNotFound = false;
          }
      }
  }
  // console.log(thisLoc);
  
  if (thisLoc && doc && doc.tag && doc.tag.vulgar_words && doc.tag.vulgar_words == 'True') {
      if (doc.tag.vulgar_words_used) {
          var vulgar_words_used = doc.tag.vulgar_words_used;
          var vulgar_words_freqs = {};
          // console.log(vulgar_words_used);
          for (var j=0; j < vulgar_words_used.length; j++) {
              var vulw = vulgar_words_used[j];
              if (Object.keys(vulgar_words_freqs).includes(vulw)) {
                  vulgar_words_freqs[vulw] += 1;
              } else {
                  vulgar_words_freqs[vulw] = 1;
              }
          }
          // console.log(vulgar_words_freqs);
          emit(thisLoc, vulgar_words_freqs);
      } else {
          console.log('error1');
      }
    } else {
        console.log('error2');
    }
}
```

### Reduce

```
function(keys, values, rereduce) {
  var all_freqs = {};
  for(var i = 0; i < values.length; i++) {
      var vulgar_words_freqs = values[i];
      // console.log(vulgar_words_freqs);
      for(var vulw in vulgar_words_freqs) {
          var freq = vulgar_words_freqs[vulw];
          if (Object.keys(all_freqs).includes(vulw)) {
              all_freqs[vulw] += freq;
          } else {
              all_freqs[vulw] = freq;
          }
        }
  }
  // console.log(all_freqs);
  // var array = [];
  // for (var word in all_freqs) {
  //   array.push({text: word, value: all_freqs[word]});
  // }
  return all_freqs;
  // return array;
}
```


## View: vulgarWordFreqAU

This MapReduce function returns vulgar word frequencies in Australia.

### Map
```
function (doc) {
  if (doc && doc.tag && doc.tag.vulgar_words && doc.tag.vulgar_words == 'True') {
      if (doc.tag.vulgar_words_used) {
          var vulgar_words_used = doc.tag.vulgar_words_used;
          for (var j=0; j < vulgar_words_used.length; j++) {
              var vulw = vulgar_words_used[j];
              emit(vulw, 1);
          }
      }
  }
}
```

### Reduce
_sum


## View: hashtagFreq

This MapReduce function returns hashtag frequencies in each state.

### Map
```
function (doc) {
  if (doc.place && doc.place.full_name) {
      var loc_l = doc.place.full_name.toLowerCase();
      var loc = doc.place.full_name;
  }
  if (doc.user && doc.user.location) {
      var loc2_l = doc.user.location.toLowerCase();
      var loc2 = doc.user.location;
  }
  var stateNotFound = true;
  var abbres = {'act': 'ACT', 'victoria': 'VIC', 'new south wales': 'NSW', 'northern territory': 'NT', 'queensland': 'QLD', 'tasmania': 'TAS', 'western australia': 'WA', 'south australia': 'SA'};
  var thisLoc = null;
  for (var abbre in abbres) {
      if  ( ( loc_l && loc_l.includes(abbre) ) || ( loc2_l && loc2_l.includes(abbre) ) ) {
          thisLoc = abbres[abbre];
          stateNotFound = false;
      }
  }
  if (stateNotFound) {
      for (var abbre1 in abbres) {
          if  ( ( loc && loc.includes(abbres[abbre1]) ) || ( loc2 && loc2.includes(abbres[abbre1]) ) ) {
              thisLoc = abbres[abbre1];
              stateNotFound = false;
          }
      }
  }
  // console.log(thisLoc);
  
  if (thisLoc && doc && doc.entities && doc.entities.hashtags) {
      var hashtags_freqs = {};
      var hashtags = doc.entities.hashtags;
      for (var j=0; j < hashtags.length; j++) {
          var hashtag = hashtags[j].text;
          if (Object.keys(hashtags_freqs).includes(hashtag)) {
              hashtags_freqs[hashtag] += 1;
          } else {
              hashtags_freqs[hashtag] = 1;
          }
      }
      emit(thisLoc, hashtags_freqs);
  }     
}
```

### Reduce

```
function(keys, values, rereduce) {
  var all_freqs = {};
  for(var i = 0; i < values.length; i++) {
      var vulgar_words_freqs = values[i];
      // console.log(vulgar_words_freqs);
      for(var vulw in vulgar_words_freqs) {
          var freq = vulgar_words_freqs[vulw];
          if (Object.keys(all_freqs).includes(vulw)) {
              all_freqs[vulw] += freq;
          } else {
              all_freqs[vulw] = freq;
          }
        }
  }
  // console.log(all_freqs);
  // var array = [];
  // for (var word in all_freqs) {
  //   array.push({text: word, value: all_freqs[word]});
  // }
  return all_freqs;
  // return array;
}
```

## View: hashtagFreqAU

This MapReduce function returns hashtag frequencies in Australia.

### Map
```
function (doc) {
  if (doc && doc.entities && doc.entities.hashtags) {
      var hashtags = doc.entities.hashtags;
      for (var j=0; j < hashtags.length; j++) {
          var hashtag = hashtags[j].text;
          emit(hashtag, 1);
      }
  } 
}
```

### Reduce
_count

