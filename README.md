# Pokemon_Go_API
Pokémon GO API in Python

# Some Info:
1. GitHub issues are mainly for bug reporting.  
2. One goal of the project is to understand the API and to give other developers a starting point.   
3. We are discussing the release but there are some problems. One point is the usage of the Pokemon GO API. We dont want Niantic to take action against API usage. There are a lot of nice projects out there built on the API. So please dont blame us about thinking about our actions.

# To-Do:
- [x] Eat moro Protobuf..
- [x] Login as pokemon trainer + token
- [x] Login over google + token
- [x] Run to pokestops
- [x] Farm specific area for pokestops
- [x] Human walking logic
- [x] Catch Pokemon automatically
- [x] Drop items when bag is full
- [x] Scan your inventar for XYZ CP pokemon and release them
- [x] Pokemon catch filter
- [x] Hatch eggs
- [ ] Incubate eggs
- [ ] Evolve pokemons
- [ ] Use candy
- [ ] Clean code
- [x] Fully automate this script
- [ ] Make v1.0 public!

# Preview:

![Alt text](etc/screen.png?raw=true "result screen")

![Alt text](etc/bot.png?raw=true "result screen")

# Video of the Pokestop farmer beta v1.0:

[![Alt text](http://img.youtube.com/vi/i1UmYyntz8A/0.jpg)](http://www.youtube.com/watch?v=i1UmYyntz8A "Pokemon_Go_API Pokestop farmer")

# Video of the Pokemon catcher v1.0:

[![Alt text](http://img.youtube.com/vi/rtGyUPhrGY0/0.jpg)](http://www.youtube.com/watch?v=rtGyUPhrGY0 "Pokemon_Go_API Pokestop farmer")

Features:
- working with google & ptc login
- fake location
- set distance for farming
- good logic to prevent bans
- automatic catching pokemons
- automatically farm pokestops 

# Requirements:
- python 2.7
- requests
- protobuf
- geopy
- s2sphere
- gpsoauth (unix)

# Credits:
- Mila432
- https://github.com/tejado for public proto
