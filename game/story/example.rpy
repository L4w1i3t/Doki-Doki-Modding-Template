# Demo file for demonstration
# This file shows how to create a basic story for your mod

label story:
    stop music
    scene black
    pause 1.0

    "Welcome to the Doki Doki Modding Central Template demo."
    label choice:
    menu:
        "Please select a mode to play through."
        "ModCen Template Tutorials":
            jump modcen_tutorials
        "{i}Mazda{/i}":
            jump mazda
    return

label modcen_tutorials:
    "We are currently working on tutorials for the ModCen Template."
    "Please be patient."
    jump choice

label mazda:
    "{i}Mazda{/i} is a small demo story for the ModCen Template."
    "Please sit back and enjoy it."
    window hide
    pause 2.0
    play music gr
    pause 1.0
    scene bg res_grayscale with dissolve_scene_full
    $ mo_name = "???"
    window auto
    mo "..."
    "My sighs echo across the realm of stillness. My batting eyes, lost in a trance of thought."
    "I continue my metronomic pace, each step seemingly attracted to the puddles and potholes that litter the road."
    "{i}At least it stopped raining,{/i} I think to myself, the shoulders of my coat weighing me down with its collected water."
    "My recently opened gash on the back of my right hand stings without letup."
    "I stop to take a look at it, where the blood has dried up and the wound is now a dark red."
    "It was when I paused my walking pace when I was interrupted by somebody drifting to my side."
    show matsuda 1b1 at l11
    show matsuda at f11
    $ ma_name = "Girl"
    ma "You okay, mate...?"
    show matsuda 1y at t11
    "I glance at the girl, Matsuda, without saying anything, almost like my brain is buffering."
    $ ma_name = "Matsuda"
    "She glares with a concerned look, her eyes darting between my hand and my face."
    "I look off into the distance before speaking."
    mo "...Yeah, just a bit of a tough day, that's all."
    mo "Nothing to really worry about. Seriously."
    "Matsuda rubs the ridges of her nose and shakes her head."
    show matsuda 1t at f11
    ma "It's Mika, isn't it?"
    show matsuda 1p at t11
    "A beat passes."
    show matsuda 1t at f11
    ma "You've really got to stop letting her do these things to you, Morgan."
    $ mo_name = "Morgan"
    show matsuda 1p at t11
    mo "...Easier said than done, you know."
    mo "It's not like anyone will do anything. She's the cheer captain and she has her little goons all the time."
    "Matsuda rolls her eyes at me."
    "Clearly, saying that was not the right answer to her."
    show matsuda 1m at f11
    ma "You know, you could always just tell the teachers."
    ma "Or a coach."
    ma "Or...I dunno, any trusted adult?"
    show matsuda 1i at t11
    "Something boils inside me, practically begging to be released."
    mo "You think I haven't tried that?"
    "Matsuda blinks twice in rapid succession."
    mo "People {i}know{/i} just how much of a bully she is, but news flash: nobody cares."
    mo "She could set me on fire or shoulder check me in public, saying crap like {i}\"Not my fault the school's mine for the slammin\',\"{/i} and nobody would bat an eye."
    mo "...Oh wait, she did that last one. TWICE."
    mo "And the moment I defend myself? Guess who gets detention for a week? I'll give you three tries."
    show matsuda 1m at f11
    ma "Morgan..."
    "She places one of her gloved hands on my shoulder and locks her eyes with mine."
    ma "This is eating you alive, isn't it?"
    ma "And you feel like you have no allies?"
    ma "No...friends?"
    show matsuda 1i at t11
    "She uses her other hand to point at herself."
    "My poker face isn't doing anyone any favors."
    mo "...Sometimes I feel like I want to kill her."
    mo "I go to school, get a bite taken out of me, return home, wallow, sleep, rinse, and repeat."
    "My voice shakes as I speak, in the most delirious sense."
    mo "Sometimes I think the world would be a better place without her."
    "Matsuda blinks once. Slowly. The corner of her mouth twitches—not quite a smile."
    "She takes her hand off my shoulder and steps back."
    show matsuda 1c at f11
    ma "I'm really glad you trust me enough to confide in me, Morgan."
    show matsuda 1m
    ma "But...we need to do something about this regardless."
    ma "Between comfort and a solution, I think we both know which one is more important, m\'kay?"
    show matsuda 1i at t11
    "My baggy eyes dart between Matsuda's face and the ground."
    "My left foot picks itself up and I take a brief step forward."
    mo "...Can we just drop this for now?"
    mo "You know how I get when I have wet clothes on my skin..."
    "Almost against my judgment, she begins walking with me and trying to match my cadence."
    show matsuda 1c at f11
    ma "Message received."
    show matsuda 1a at t11
    "She gives me a small, understanding smile before pausing in her dialogue."
    mo "...So, uh, what are you even doing out here?"
    mo "Shouldn't you be heading the other way or something?"
    show matsuda 1c at f11
    ma "I know."
    ma "Buuuuuuut, I was thinking...what if I met you over at {i}your{/i} place?"
    ma "Tu casa, mi casa, or something like that, right?"
    show matsuda 1a at t11
    mo "That's not how that saying goes, but I get what you're putting down..."
    mo "I mean, I guess you can come over."
    "I ever so briefly let out a chuckle at the absurdity of Matsuda inviting herself over."
    "{i}Not the first time she's done this, but I'll never get used to it.{/i}"
    mo "You know my house is boredom central, though. Why even bother?"
    show matsuda 1c1 at f11
    ma "...Because you're my friend, duh doy."
    ma "And I want to help you."
    ma "...And it's the weekend."
    ma "...Aaand I don't have any plans."
    ma "...Aaaaaand-"
    show matsuda 1x at t11
    "I cut her off before she can continue."
    mo "Okay, okay, I get it."
    mo "Yeah, sure, you can, uh, do something then."