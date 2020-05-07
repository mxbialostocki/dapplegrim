# DEATH
the instance in which the player comes to the end of their story. There are three kinds of death - groups of death scenarios for each of the characters. Some of them contain multiple options:
death: {
  thischaracter: {
    fieldDeath: "gristly",
    dreamDeath: "soft but unexpected",
    mountainDeath: {
      scenarioOne: "scenario one death is deadly red",
      scenarioTwo: "scenario two death is purple and green"
    },
    
  }
}
# THE ROOM
the unnamed room in which the player wakes, staring straight into your reflection's eyes

# THE MOUNTAIN
only dapplegrim and servant go here, but the king visits the mountain in a dream

# KING'S THRONE ROOM
several decisions are made here

# CASTLE FIELDS
all three characters interact with the field

# THINGS
things: {[
  'mares',
  'foals',
  'field',
  'king',
  'dapplegrim',
  'servant',
  'brothers',
  'moon',
  'princess',
  'inheritance',
  'deaths'
]}

# PLAYERS
## Girl
You wake in the night to find the young Prince's Witch hunters attacking your small farm. Your horse helps you escape to a field, but is hunted down and killed while you hide in the forest. Standing ina moonlit field at six years old you cast dark arts, covered with the Horse's blood until the prince witchhunter finds you and cleaves you in two. With your dying breath you curse the prince, watching the moon mistress smile down upon you. But does she turn red, or does your blood drip over the princes eyes?
## King
As a young prince you hunt usurpers for your mommy and burn them as witches. One night you cleave and entire family, but your mommy falls sick and you retire to srve your kingdom. You gift the farm of the last family of witchhunters to an old soldier with twelve sons. Yet your mind goes as a field of red wheat ages and begins to eat the forest surrounding you. Eventually your saviour comes in the form of a young servant in possession of strange powers... and a demon horse that begins to threaten your sanity.
## Dapplegrim
You wake covered in viscera atop a mountain, barely conscious of what you might be... your brothers and sisters gather around as a vertical skin creature approaches your mamas. Yet you become jealous and when they look into your eyes..... you slaughter your family. you are left alone but you call, call for your other body - it is yours. You seek a vengeance you don't know the name of. Your other body comes more easily, next time...
## Servant
You leave home to avoid fraternal abuse and find a job as a servant in the kings castle. But the king is going slowly mad and when you visit home after a couple of years your fortunes have worsened. Your brothers have killed your parents and taken your inheritance, but leave you twelve mares living wild in the mountains. Each mare has had a foal, you choose between two foals, bad things happen, ad! bad! the blood... Eventually Dapplegrim rules the kingdom.

# STRUCTURE
structure: {
  Map
  Engine
  Scene: {
    Death
    Room
    Farm
    King's Room
    Foal-Cursing Circle Field
    Mountain
    Throne Room

  }
}