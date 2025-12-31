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
        #"ModCen Template Tutorials":
            #jump modcen_tutorials
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
    "I briefly let out a chuckle at the absurdity of Matsuda inviting herself over."
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
    mo "Yeah, okay, whatever, I get it."
    mo "Yeah, sure, you can, uh, do something then."
    show matsuda 1a
    "Matsuda gives me a thumbs up and grins."
    show matsuda 1z at f11
    ma "Hey, maybe we can binge that weird anime you like, the one with the racing horses?"
    ma "What was it called again? I'm only, like, an episode in."
    show matsuda 1x at t11
    mo "...{i}Amumasame{/i}. And it's not weird, it's awesome."
    mo "\'Sides, believe it or not, it helps me think more about track."
    show matsuda 1o1 at f11
    ma "...Whatever helps you sleep at night, mate."
    scene black with wipeleft_scene
    "The two of us continue our less-than-brisk pace, the mood now more comfortable."
    "It starts to sprinkle again, enough to mistify the horizon, and the arms of Matsuda's still-tidy blazer begin to dampen with happily meek droplets."
    "I inadvertently stomp my left shoe right into a pothole, muddying both it and my sock."
    "{i}Aaagh, damn...{/i}"
    "{i}I just wanna throw my shoes off...{/i}"
    "With so many minor irritations, one would think I'd crack, but...I just feel mellow."
    "I look over at Matsuda, who is now humming a tune ever so eternal."
    "{i}...Lacrimosa.{/i}"

    scene bg house_grayscale with dissolve_scene_full
    "Our quaint yet punctual gaits are joined by a new instrument of my dog's barking through the window as we approach my front gate."
    "I take a muddied breath as I pry it open, almost like I have something in my throat."
    show matsuda 1z at f11
    ma "You good?"
    ma "This is your own crib, not a firing squad."
    show matsuda 1x at t11
    mo "...I'm totally tubular, thanks for asking."
    show matsuda 1c at f11
    ma "Radical."
    show matsuda 1a at t11
    "She flashes me a quick \'hang loose\' gesture."
    "The dog persists in its barking as he watches us fool around before the doorstep."
    "I feel up and down my pockets."
    mo "...Matsuda."
    show matsuda 1b
    mo "Give me my keys back."
    show matsuda 1f at f11
    ma "...Huh?"
    show matsuda 1b at t11
    "Her expression is that of genuine confusion."
    "{i}What do you mean, you didn\'t pickpocket me?{/i}"
    mo "...Do you not have them?"
    show matsuda 1f at f11
    ma "No? Why would I have something that\'s yours?"
    show matsuda 1b at t11
    "I blush slightly out of mortification."
    "I run my hands through my pockets again."
    "Front, back, jacket, nothing but my phone and a crumpled up receipt from the corner store."
    mo "Don\'t tell me I..."
    "I unzip and scramble through my bag."
    "No jingling to be heard."
    mo "...Fuuuuuuuuuuuuuuuuuudge."
    "I hang my head, looking up, and sigh."
    mo "So, turns out...I may or may not have forgotten the ONE thing I need in my locker."
    show matsuda 1e at f11
    ma "...Wait, wait, wait. You\'re telling me we walked all this way—" 
    ma "—in the rain—" 
    ma "—with you whining about your soggy shoes—"
    show matsuda 1fp
    ma "...and you don\'t even have your keys?!"
    show matsuda at t11
    "I rub the back of my neck, pretending to care less than I probably should."
    mo "Guess not."
    show matsuda at f11
    ma "Mate, how do you forget that kinda thing?"
    show matsuda at t11
    "Her voice spikes with incredulity, but I just shrug."
    mo "Easy. You\'d be surprised what you can forget when you\'re running on fumes."
    "I let out a weak chuckle, half-sincere, half to fill the silence."
    show matsuda 1b1 at f11
    ma "...You\'re too calm about this."
    show matsuda 1y at t11
    mo "What\'s the point of freaking out? Life takes its shot, the universe rebounds, I foul out. Same old game."
    "I lean against the fence, staring at the mist curling off the pavement."
    "Matsuda\'s shoulders sink, her earlier fire cooling to something gentler."
    show matsuda 1b1 at f11
    ma "...That\'s not how it\'s supposed to be, y\'know."
    show matsuda 1y at t11
    mo "Yeah, well, supposed-to and reality are two different things."
    "My dog keeps barking through the window, oblivious to the irony."
    show matsuda 1f at f11
    ma "So...what now?"
    show matsuda 1b at t11
    "I glance down at the mat before the front door and rub my foot across it."
    mo "...My backup key."
    show matsuda 1fp at f11
    ma "Bruh."
    show matsuda at t11
    mo "Never said I didn\'t have one."
    show matsuda 1fp at f11
    ma "Yeah, but the universal implication earlier that--"
    ma "...Nevermind, whatever."
    show matsuda at t11
    "I reach down, pull up the mat, and retrieve a small, somewhat rusty key taped to the underside."
    show matsuda 1b
    mo "As for my main set... That\'s an issue for tomorrow me."
    window hide(None)
    stop music
    scene black
    play sound door_open
    pause 2.0
    play sound door_close
    scene bg kitchen_grayscale with wipeleft_scene
    window auto
    play music cry
    mo "Heyyyyyy there, Suzie~"
    "I kneel down and begin to wiggle and coax my dog, Suzie, who is now frantically wagging her tail and licking my face."
    "She looks eagerly at Matsuda, who made a beeline for the couch in the other room."
    show matsuda 2c at f44
    ma "Hey Suzie..."
    ma "Look what I got~"
    show matsuda 2a at t44
    "Matsuda pulls out and waves a small dog biscuit."
    mo "Ah, there it is."
    "I snap my fingers in the direction of the other room, and the dog follows suit and catches the treat midair from Matsuda tossing it almost enough to hit the ceiling."
    show matsuda at thide
    hide matsuda
    ma "Now...LEAP OF FATH!!!"
    "Matsuda dashes into the living room and swan dives onto the couch, knocking the pillows onto the floor."
    mo "...Okay then."
    mo "Want a snack or anything?"
    ma "Not hungry, brochacho."
    "I shrug and take my shoes off."
    mo "Suit yourself. As for me, I\'m headed upstairs."
    mo "Got an unfinished save file calling my name."
    "Matsuda bounces off the couch like a mannequin and jolts back over to me."
    show matsuda 1f at l41
    show matsuda at f41
    ma "Oh dang, what game?"
    show matsuda 1q 
    ma "Friggin\' {i}Amu-{/i}whatever-the-flip or whatever?"
    show matsuda 1o at t41
    mo "...No, actually. Have you not heard of {i}Pillars of the Elden Doki: Megami Legend of Fantasy Quest IV Final Chapter Prologue Royal{/i}?"
    show matsuda 1m at f41
    ma "The rerelease?"
    show matsuda 1b at t41
    mo "Nah, the rerelease sucks donkey balls. I like the old-school version."
    show matsuda 1m at f41
    ma "...The original came out 6 months ago, ya geezer."
    show matsuda 1b at t41
    mo "Shut the up."
    mo "So you coming or not?"
    scene black with wipeleft_scene
    "After another minute of pointless bickering, Matsuda and I find ourselves settled in my room."
    scene bg room_grayscale with wipeleft_scene
    "The scent of tangerines pugnates the air."
    "Matsuda is sifting through my collection of half-finished games while I plug in my console with two controllers."
    mo "By the way, I got a music player in the corner over there. Just bought it last week."
    show matsuda 1c at f44
    ma "Ooooh, fancy."
    show matsuda 1a at t44
    "Without further permission, Matsuda hits the power button and starts scrolling through the tracklist."
    call show_bgm_override from _call_show_bgm_override_1

    init 2 python:
        bgm_tracks.append(("Crying Over You", audio.cry))
        bgm_tracks.append(("Abutting, Dismantling", audio.gr))

    mo "Yeah, uh, feel free to pick something if you want...or not. I don\'t care."
    show matsuda 1c1 at f44
    ma "...The heck are these names?"
    show matsuda 1x at t44
    mo "Bargain bin ones."
    mo "You playing or not?"
    "I point to my TV and the console setup."
    show matsuda 1v1
    mo "You get the third-party controller, b-t-dubs."
    "{i}Aha...this is a single-player game, and I only have this one controller.{/i}"
    scene black with wipeleft_scene
    "Matsuda and I sit shoulder-to-shoulder before my TV."
    "She insists on watching me go through a level first before diving into multiplayer, because apparently she's never played this game."
    "Humoring her, I oblige."
    stop music fadeout 0.5
    scene bg room_grayscale
    show vignette:
        alpha 1.0
    with wipeleft_scene
    "I blow on the cartridge before inserting it, and..."
    call hide_bgm_override from _hide_bgm_override_1
    window hide
    pause 3.0
    call rpg_flicker from _call_rpg_flicker
    play music gamemusic
    call rpg_start from _call_rpg_start
    stop music fadeout 0.5
    hide vignette with Dissolve(0.5)
    show matsuda 1a at t11
    window auto

    # Check if the player won or lost
    if rpg_state.game_won:
        # if the player won the game
        scene bg room_grayscale
        play music cry
        mo "...And that\'s all she wrote."
        show matsuda 1z1 at f11
        ma "Not bad! I mean...I guess that was alright."
        ma "Still nothing compared to my god gamer skills."
        show matsuda 1b2 at t11
        mo "You\'re lecturing me on a game that you haven\'t played?"
        mo "Gutsy, not gonna lie."
        show matsuda 1c at f11
        ma "Hey, don\'t forget you\'re on the other scale, what with how many hours you\'ve told me you\'ve put into gaming, ya friggin\' gremlin."
        
        # Check if player was in hidden map but didn't trigger sinister event
        if rpg_state.map and "hidden.txt" in rpg_state.map.path and not rpg_state.sinister_triggered:
            show matsuda 1f
            ma "Though, uh...did the game glitch out for a sec there?"
            show matsuda 1b at t11
            mo "...Huh? What do you mean?"
            show matsuda 1m at f11
            ma "The screen went all weird and staticky. Thought your cartridge was dying."
            show matsuda 1b at t11
            mo "Nah, it\'s probably just the console acting up."
            mo "Thing\'s older than my grandma anyway."
            show matsuda 1c at f11
            ma "Mm, fair. Anyway~"
            ma "Gotta give you credit. Kudos for pulling through!"
            ma "But, again, may just be that you\'re a massive gamer nerd with how many hundred hours."
        
        show matsuda 1a at t11
        "My mouth speaks before my brain does."
        mo "I\'m good here cause I actually have agency, obviously."
        mo "I got the controller, I make pixel do thingy on the screen..."
        mo "I mean, who\'s gonna stop me from making the character on screen doing a cannonball off a giant-ass mountain?"
        show matsuda 1c1 at f11
        ma "O...kay then."
        show matsuda 1x at t11
        mo "...Yeah, guess that got off track quick."
    elif rpg_state.game_over:
        # if the player got a game over
        scene bg room_grayscale
        play music cry
        mo "Bruh."
        show matsuda 1z at f11
        ma "Pfffffhahaha!"
        ma "Dude, you just got absolutely BODIED by a bunch of pixels!"
        show matsuda 1z1
        ma "What happened to all those hours of \'gaming experience\', huh?"
        show matsuda 1b2 at t11
        mo "Okay, first of all, rude."
        mo "Second of all, that was a tactical retreat."
        show matsuda 1z at f11
        ma "A tactical retreat? Morgan, you literally walked into the enemy and died!"
        show matsuda 1z1
        ma "That\'s not tactics, that\'s just being dogwater!"
        show matsuda 1x at t11
        
        # Check if player was in hidden map but didn't trigger sinister event
        if rpg_state.map and "hidden.txt" in rpg_state.map.path and not rpg_state.sinister_triggered:
            mo "Plus the game was glitching out anyway."
            show matsuda 1f at f11
            ma "Wait, what? When?"
            show matsuda 1b at t11
            mo "The screen went all fuzzy for a bit. Cartridge is probably corroded."
            show matsuda 1e at f11
            ma "Oh my god, you\'re blaming the CARTRIDGE now?"
            ma "Mate, you really need to stop making excuses."
            show matsuda 1z at f11
            ma "Just take the L with some dignity!"
            show matsuda 1x at t11
        
        mo "...It was a lag spike."
        show matsuda 1fp at f11
        ma "It\'s a CARTRIDGE game! There\'s no lag!"
        show matsuda 1e
        ma "You can\'t just blame random things for your skill issue!"
        show matsuda 1b at t11
        mo "Whatever. Controller\'s got drift anyway."
        show matsuda 1c at f11
        ma "Mhm, sure it is."
        ma "Just admit you got dunked on by some baddies."
        show matsuda 1a at t11
        "I roll my eyes and lean my back onto the floor."
        mo "You\'re insufferable, you know that?"
        show matsuda 1c1 at f11
        ma "And you\'re bad at video games~"
        show matsuda 1x at t11
        mo "...I hate you."
        show matsuda 1z1 at f11
        ma "And I\'m the pope."
        show matsuda 1b2 at t11
    elif rpg_state.sinister_triggered:
        # if the sinister event was triggered
        scene bg room_grayscale
        show layer master at heartbeat
        show veins
        show vignette:
            alpha 0.5
        with Dissolve(2.0)
        
        window hide
        pause 2.0
        show matsuda 1b at t11
        pause 1.5
        show matsuda 1f at f11
        pause 1.0
        show matsuda 1b at t11
        pause 2.0
        pause 1.5
        show matsuda 1m at f11
        pause 1.0
        show matsuda 1b at t11
        pause 2.5
        show matsuda 1i at f11
        pause 1.0
        show matsuda 1b at t11
        pause 3.0
        show layer master
        hide veins with Dissolve(3.0)
        
        pause 1.0
        
        window auto
    else:
        # if the player exited early (pressed ESC)
        scene bg room_grayscale
        play music cry
        show matsuda 1f at f11
        ma "Uh...Morgan? You good?"
        show matsuda 1b at t11
        mo "Yeah, yeah...just lost interest, I guess."
        show matsuda 1d at f11
        ma "That fast? You barely even started playing!"
        show matsuda 1b at t11
        mo "Eh, wasn't really feeling it."
        show matsuda 1c at f11
        ma "Alright then, fruit fly."
        show matsuda 1b at t11
    
    mo "Well, anyway, you gonna play now or...?"

    if rpg_state.sinister_triggered:
        window hide(None)
        stop music
        scene black
        pause 3.0
        show noise zorder 1000:
            alpha 1.0
            quick_flashing
        play music mscare
        pause 4.0
        hide noise
        stop music
        define weird_counter = 0
        label weird_still:
            play music rumble
            scene bg kitchen_grayscale
            show vignette zorder 9:
                alpha 1.0
            show veins zorder 10
            jump weird_choice
        label weird_choice:
            $ weird_counter += 1
            menu:
                "Left":
                    stop music
                    scene black
                    pause 3.0
                    jump weird_left
                "Right":
                    stop music
                    scene black
                    pause 3.0
                    jump weird_right
                "Still":
                    stop music
                    scene black
                    pause 3.0
                    jump weird_still
                "Her" if weird_counter >= 5:
                    stop music
                    scene black
                    pause 3.0
                    play sound door_open
                    pause 2.0
                    play sound door_close
                    scene bg room_grayscale
                    show black zorder 8:
                        alpha 0.4
                    show vignette zorder 9:
                        alpha 1.0
                    show veins zorder 10
                    show layer master at heartbeat
                    play music rumble
                    play music2 hb
                    jump weird_wtf
        
        label weird_left:
            play music rumble
            scene bg res_grayscale
            show vignette zorder 9:
                alpha 1.0
            show veins zorder 10
            jump weird_choice
        
        label weird_right:
            play music rumble
            scene bg house_grayscale
            show vignette zorder 9:
                alpha 1.0
            show veins zorder 10
            jump weird_choice

        label weird_wtf:
            # this should make the player go "what the actual heck is happening right now"
            menu:
                "Proceed":
                    stop music
                    stop music2
                    scene black
                    show veins zorder 10
                    play music horrible
                    pause 3.0
                    play sound bash
                    pause 2.0
                    play sound bash
                    pause 1.0
                    play sound bash
                    pause 2.0
                    play sound bash
                    pause 5.0
                    stop music
                    scene bg room_grayscale
                    show matsuda 1b at t11
                    jump okbackontrack

        label okbackontrack:
            play music smooth
    
    show matsuda 1c at f11
    ma "Oh, right, my turn, yeah!"
    show matsuda 1a at t11
    "I toss her the controller and she catches it without looking."
    "Immediately, she's off to the races, fingers moving across the buttons like muscle memory."
    show matsuda 1c1 at f11
    ma "Alright, let\'s see what you\'ve been hyping up..."
    show matsuda 1x at t11
    "Within the first minute, she\'s already cleared what took me three tries."
    mo "...Okay, show off."
    show matsuda 1z at f11
    ma "What can I say? Natural talent~"
    show matsuda 1a at t11
    "Suzie trots into the room and plops down next to me, resting her head on my lap."
    "I watch Matsuda play, her focus intense but casual."
    "The room fills with sound effects, button clicks, and occasional commentary from both of us."
    show matsuda 1c at f11
    ma "By the way, did you know the speedrun record for this game is, like, twelve minutes?"
    show matsuda 1a at t11
    mo "That\'s impossible. There\'s no way."
    show matsuda 1c1 at f11
    ma "Dude, I watched the video. They clip through half the walls using some frame-perfect glitch."
    ma "Absolutely bonkers."
    show matsuda 1x at t11
    mo "Huh. Sounds like something you\'d try."
    show matsuda 1c at f11
    ma "Hell yeah I would. Just gotta find the right tutorial."
    show matsuda 1a at t11
    "She pauses the game suddenly."
    "For a moment, she just stares at the screen."
    show matsuda 1m at f11
    ma "...Hey."
    show matsuda 1b at t11
    mo "...Yeah?"
    show matsuda 1m at f11
    ma "Thanks."
    show matsuda 1b at t11
    "That catches me off guard."
    mo "For what?"
    show matsuda 1m at f11
    ma "For letting me hang around today, even if I kinda just...invited myself over."
    ma "I know you probably wanted to just...I dunno, wallow or whatever."
    show matsuda 1i
    ma "But I'm glad I came over anyway."
    show matsuda 1b at t11
    "There's something unspoken in the way she says it."
    "Like she's relieved I'm still here, breathing and existing."
    mo "...Yeah. Same."
    show matsuda 1c at f11
    ma "Radical."
    show matsuda 1a at t11
    "She unpauses the game and continues playing."
    scene black with wipeleft_scene
    "Hours blur together."
    "We play, we talk, we don\'t talk, and we laugh with some weird stories about when we were in grade school."
    "At some point, Matsuda orders pizza on my phone without asking, and I don\'t even protest when she gets pineapple on it."
    "The rain never fully stops, it just oscillates between drizzle and downpour."
    scene bg room_grayscale with wipeleft_scene
    show matsuda 1a at t11
    "Eventually, the room darkens as evening sets in properly."
    "Matsuda checks her phone and groans."
    show matsuda 1e at f11
    ma "Ughhh, it\'s already past nine."
    ma "Dad\'s gonna kill me if I\'m not back soon."
    show matsuda 1b at t11
    mo "You could just stay over."
    show matsuda 1f at f11
    ma "And deal with him blowing up my phone all night? Hard pass."
    show matsuda 1m
    ma "Besides, you need some alone time anyway. I can tell...I think."
    show matsuda 1b at t11
    "She\'s not wrong."
    "As much as I appreciate her being here, there\'s a part of me that\'s been waiting for the usual solitude."
    mo "...Yeah."
    show matsuda 1c at f11
    ma "See? I know you too well, fruit fly."
    show matsuda at thide
    hide matsuda
    "She stands and stretches, joints popping audibly."
    scene black with wipeleft_scene
    "I walk her downstairs. Suzie follows, tail wagging and oblivious."
    scene bg kitchen_grayscale with wipeleft_scene
    show matsuda 1a at t11
    "Matsuda pulls her shoes back on--still damp from earlier--and grimaces."
    show matsuda 1e at f11
    ma "Eugh, wet socks. The worst timeline."
    show matsuda 1b at t11
    mo "Should\'ve brought an extra pair."
    show matsuda 1c1 at f11
    ma "Should\'ve, would\'ve, could\'ve."
    show matsuda 1a at t11
    "She grabs her bag and slings it over her shoulder."
    "For a moment, she just stands there, looking at me with an expression I can\'t quite read."
    show matsuda 1m at f11
    ma "...Don\'t do anything stupid while I\'m not here, yeah?"
    show matsuda 1b at t11
    mo "Define stupid."
    show matsuda 1c at f11
    ma "You know what I mean."
    show matsuda 1a at t11
    mo "...Yeah. I know."
    show matsuda 1c1 at f11
    ma "Good. \'Cause I\'ll see you Monday, and I expect you to still be in one piece."
    show matsuda 1x at t11
    mo "No promises."
    show matsuda 1e at f11
    ma "Morgan."
    show matsuda 1b at t11
    mo "...Fine. One piece. Got it."
    show matsuda 1c at f11
    ma "That\'s the spirit."
    ma "Also One Piece menti-{w=0.5}{nw}"
    show matsuda 1a at t11
    ma "NOPE, shut up, I know you were gonna go there."
    show matsuda 1c at f11
    ma "Anyway, later gator."
    show matsuda at thide
    hide matsuda
    "She gives me a mock salute and heads out into the night."
    window hide(None)
    play sound door_close
    scene black
    pause 2.0
    scene bg room_grayscale with dissolve_scene_full
    window auto
    "The house feels different when she\'s gone."
    "I mean, goes without saying, plus I\'m used to being alone, but..."
    "The best way I can describe it is the way something feels the immediate moment after a party ends."
    "I trudge back upstairs, Suzie at my heels, and collapse onto my bed."
    "The console is still on, the pause screen glowing faintly in the now dim room."
    "I should turn it off. Save electricity or whatever."
    "But I don\'t."
    "Instead, I just lie there, staring at nothing."
    "My hand throbs dully. The cut from earlier has scabbed over, but it\'s tender to the touch."
    "{i}Monday\'s gonna suck.{/i}"
    "{i}But that\'s a problem for future me.{/i}"
    "I close my eyes, willing sleep to come."
    "It doesn\'t."
    "My brain won\'t shut off, replaying the day on loop."
    "The usual sneers at me, the rain, Matsuda\'s concern, the game, the pizza, the social convention..."
    "{i}Maybe I should try to have more of these days...{/i}"
    "{i}Ones that have a nice little treat at the end that I can look forward to.{/i}"
    scene black with dissolve_scene_full
    "I roll over, burying my face in the pillow."
    "Suzie shifts beside me, her warmth a small comfort."
    "The rain picks up again outside, drumming against the window."
    "Eventually--maybe an hour later, maybe five minutes, I don\'t keep track--I reach for my phone out of habit."
    "{i}Just a quick scroll before bed. That\'s all.{/i}"
    "The first thing I see is a news alert on a social media platform..."
    "{i}\"Mika **********, age **, found dead in her home this afternoon as the result of a sudden heart attack, police say.\"{/i}"
    window hide
    # END
    pause 3.0
    scene end with dissolve_scene_full
    pause 3.0
    stop music fadeout 2.0
    scene black with dissolve_scene_full
    pause 2.0
    window auto
    "Yo. ModCen team here."
    "See how easy it is to make a mod story?"
    "Sure, it gets more nuanced as you add features and addons and such, but at a base level, all you need is knowhow and an idea."
    "Don\'t be afraid to take risks and try new things with your stories."
    "And hey, even if it ultimately doesn\'t work out, you can always learn and try again."
    "Thanks for playing!"