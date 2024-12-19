import time
import random


def beeping_alarm():
    while True:
        for i in range(3):
            print("BEEP BEEP BEEP")
            time.sleep(1)
        userChoiceGetUp = input(
            "'T' to turn off the alarm or any other button to snooze: ")
        if (userChoiceGetUp.lower() == "t"):
            print("Turned Alarm Off")
            break
        else:
            print("Snoozed Alarm")
    return None


naratives = {
    # You wake up
    0: {
        "text": """You get up out of bed, you know you have about {dayLeftToApply} to find a new job You feel kinda excited but
    Want to get a job already and not have to apply to so many jobs. But someone has to pay the bills
    and that has to be you. You head to the bathroom and brush your teeth. And then head to
    the kitchen to eat breakfast.You open you pantry and see: bread, eggs, frostedflakes, chips
        What do you eat?
        1) Bread
        2) Eggs
        3) Frosted Flakes
        4) None""",
        "effects": {
            1: {"health": 5},
            2: {"health": 10, "motivation": -2},
            3: {"health": 2, "motivation": -1},
            4: {"health": -3}
        },
        "next":{1: 1, 2: 1, 3: 1, 4: 1}
    },

    # Work at office or back to bed
    1: {
        "text": """You leave the room and head back to the hallway. You see your bedroom with your confortable bed and your office
    with your 3 monitor set up. You know you have to apply for jobs and keep up with homework. But your bed looks so comfortable.
    What do you do? (P.S. The back of your head is telling you to get your butt up and work like when you are making this program) 
    1) Office
    2) Bed""",
        "effects": {
            1: {"motivation": 5, "chanceOfJob": 10},
            2: {"health": -1, "motivation": -8, "chanceOfJob": -30, "dayLeftToApply": -1},
        },
        "next":{1: 1.1, 2: 99.1}
    },

    # APply for jobs or study
    1.1: {
        "text": """You sit down at your computer and think what you need to do to get a CS job. It has been so hard because of AI
        has been taking so many jobs. It is so comptive and a little discouring. 
        What do you want to do?
        1) Look on linkedin for jobs to apply
        2) Study a topic that you can put on your resume
        3) Go back to bed""",
        "effects": {
            1: {"motivation": 2, "knowledge": 1, "chanceOfJob": 10},
            2: {"motivation": 5, "knowledge": 6, "chanceOfJob": 3},
            3: {"health": -1, "motivation": -8, "chanceOfJob": -30, "dayLeftToApply": -1},
        },
        "next": {1: 1.2, 2: 2, 3: 99.1}
    },

    # Ah, good old linkedin
    1.2: {
        "text": """You look through LinkedIn and find two types of job that over 150 have already applied for:
        1) A perfect job that fits your skills exactly (rare).
        2) A job that you qualify for but requires studying in a topic (AWS/Docker/Azure/Snowflake/etc).
        3) Give up and go back to bed.""",
        "effects": {
            1: {"motivation": -10, "chanceOfJob": 30},
            2: {"motivation": -5, "knowledge": 10, "chanceOfJob": 20},
            3: {"motivation": -3, "chanceOfJob": -10}
        },
        "next": {1: 1.3, 2: 2, 3: 99.1}
    },

#2 have it be studying

    # Having to tailor the resume every single time. Bruh
    1.3: {
        "text": """You find a job posting that seems like a good (that 90 other people thought the same things). 
        But not withstanding competiting against all the CS master degree people with 40 years of experience,
        You're excited to apply and begin the process. But you read the job description, you realize you need to update 
        your resume to tailor it.
    What do you do?
    1) Update your resume
    2) Procrastinate and do it later and go to bed""",
        "effects": {
            1: {"motivation": -5, "chanceOfJob": 5},
            2: {"motivation": -10, "chanceOfJob": -5}
        },
        "next": {1: 1.4, 2: 99.1}
    },

    # Update Resume
    1.4: {
        "text": """You pull up your resume, spending a good amount of time updating your skills, 
        formatting, and making sure everything is accurate. After a while, you’re finally ready to apply. 
    What do you do?
    1) Proceed with the application
    2) Procrastinate and do it later and go to bed""",
        "effects": {
            1: {"motivation": -5, "chanceOfJob": 10},
            2: {"motivation": -10, "chanceOfJob": 0}
        },
        "next": {1: 1.5, 2: 99.1}

    },

    1.5: {"text": """You log into the company's application portal, so so excited to update your resume and be
        done with that job application that you spend way to long on. only to find out that, despite uploading your resume, 
        you still have to manually fill in all your details again. for the 80th time. Bruh, why do you even need a 
        resume anymore.
        What do you do?
    1) Push through and fill it all out
    2) Dude, just give up. Just get into bitcoin or start a almost illegal primide scheme.""",
        "effects": {
                1: {"motivation": -10, "chanceOfJob": 5},
                2: {"motivation": -20, "chanceOfJob": -5}
        },
        "next": {1: 1.6, 2: 99.1}
        },

    # Ah, Cover letters
    1.6: {
        "text": """You get to the next part of the application, after spending even more time filling
     the information already on your resume to there application website. And only to realize they 
     require a cover letter. You are not happy. But now it’s time to write one.
    What do you do?
    1) Write the cover letter
    2) Skip it and hope it’s optional""",
        "effects": {
            1: {"motivation": -10, "knowledge": 5, "chanceOfJob": 10},
            2: {"motivation": -5, "chanceOfJob": -15}
        },
        "next": {1: 1.7, 2: 1.8}

    },

    # Spending time to write the cover letter
    1.7: {
        "text": """You spend time researching about the company and other BS you can find to make it sound
    like you spend a lot of time researching there company, when in reality you just use chatgpt to learn about them
    and look at the reviews to see how much of a sweatshop that company is.
    What do you do?
    1) Spend time researching the company
    2) Write a generic cover letter without research""",
        "effects": {
            1: {"motivation": -5, "knowledge": 10, "chanceOfJob": 15},
            2: {"motivation": -3, "chanceOfJob": -5}
        },
        "next": {1: 1.8, 2: 1.9}

    },

    1.8: {
        "text": """I spend now over 2.5 hours applying for one job. Yay. I am so happy. I love the world. I am filled with
    so much joy. I love making resumes and cover letter and will probably not hear anything back. But, anyway, should
    i double ckekc speleing on my resuame? 
    What do you do next?
    1) Review it once more before submitting
    2) Submit it right away""",
        "effects": {
            1: {"motivation": -2, "chanceOfJob": 5},
            2: {"motivation": 0, "chanceOfJob": 0}
        },
        "next": {1: 1.9, 2: 1.9}

    },

    1.9: {
    "text": """WOW, Congudations, you just spend 3 hours on applying for one job. You must feel proud. *Clap*. *Clap*. *Clap*.
    Well, based on everything you have experinced so far, do you think you will hear back?
    What do you expect?
    1) Doubt you will hear anything back
    2) Doubt you will hear anything back""",
    "effects": {
        1: {"motivation": -5},
        2: {"motivation": -10},
    },
    "next": {1: 1.1, 2: 1.1}
},

    # Studying
    2: {
    "text": """Well look at this! you decide to spend some time studying. 
    You pull up a few tutorials and videos on topics that you know 
    will help you stand out in the competitive job market. Good job you!
    What topic do you want to study my guy?
    1) AWS
    2) Docker
    3) Kubernetes
    4) Microsoft Azure""",
    "effects": {
        1: {"knowledge": 10, "motivation": -2, "chanceOfJob": 5},
        2: {"knowledge": 8, "motivation": -2, "chanceOfJob": 4},
        3: {"knowledge": 12, "motivation": -3, "chanceOfJob": 6},
        4: {"knowledge": 9, "motivation": -2, "chanceOfJob": 5}
    },
    "next": {1: 2.1, 2: 2.1, 3: 2.1, 4: 2.1}
    },

    2.1: {
    "text": """After studying for a few hours, you improved your skills, 
    but youre drained. What do you do next?
    1) Go to bed
    2) Keep studying more topics to get ahead
    3) Look for jobs to apply with your new skills""",
    "effects": {
        1: {"motivation": -10, "chanceOfJob": -5},
        2: {"knowledge": 5, "motivation": -5, "chanceOfJob": 2},
        3: {"motivation": -2, "chanceOfJob": 10}
    },
    "next": {1: 99.1, 2: 2, 3: 1.2}
},

    # You went back to bed
    99.1: {
        "text": """You look at your bed, your best friend, and did not want to leave it there being cold. You tell yourself you will
        only go back to sleep for 5 minuites, it will be fine.... You set your alarm for 15 minutes and look forward to waking up with 
        more energy!!!.......

        You wake up well rested, and the you look at your phone it is 1 hour eariler since you woken up first. How could that be?? you tell 
        yourself, and then you check the day and realized you sleeped for a whole 23 hours. Impressives. Feeling dispointed that you missed a 
        whole days worth of work, you tell yourself either you work or go back to bed. what do you do?
    1) Office
    2) Bed""",
        "effects": {
            1: {"motivation": 3, "health": 2},
            2: {"health": -1, "motivation": -8, "chanceOfJob": -30}
        },
        "next":{1: 1, 2: 0}
    },

    997:  {
    "text": """You slump into the couch, Netflix starts autoplaying another episode, 
    and you can’t remember the last time you left the house.
    What do you do now?
    1) Order food and binge-watch TV
    2) Close your eyes and try to sleep""",
    "effects": {
        1: {"motivation": -100, "health": -20},
        2: {"motivation": -100, "health": -10}
    },
    "next": {1: 1004, 2: 1002}
},
    
    999: {"text": """You wake up and check the date—today is the last day before your financial situation forces you to stop job hunting.
    You feel a sense of dread as you realize there no time left. You are so scured The bills are piling up, and your bank account has dwindled.
    What do you do now?
    1) Look for last-minute freelance gigs online
    2) Give up and accept your fate""",
    "effects": {
        1: {"motivation": -10, "chanceOfJob": -30},
        2: {"motivation": -100, "chanceOfJob": -100}
    },
    "next": {1: 1000, 2: 1001}
},

1000: {
    "text": """You find a last gig that barely pays cover a week's worth of expenses.
    It's not sustainable, but it buys you a bit more time. Can you keep this up?
    Nope
    GAME OVER
    You're to broke my dude. sorry about that""",
    "effects": {}
},
1001: {
    "text": """You decide to give up. The weight of responsibility becomes too much, you to move back
    in with family or friends. You feel like you've lost control of your life.
    GAME OVER""",
    "effects": {}
},
1002:{
    "text": """You ordering food and binge-watching. you don't even remember the last time you applied for a job.
    GAME OVER""",
    "effects": {}
},
1003:{
    "text": """You close your eyes and fall into a deep sleep, dreaming of a different life where things aren’t so overwhelming.
    GAME OVER""",
    "effects": {}
}
}

game_state = {
    "dayLeftToApply": 5,
    "health": 35,
    "motivation": 60,
    "chanceOfJob": 100,  # out of 1000 maybe?
    "knowledge": 20
}

def save_game_to_file(filename):
    with open(filename, 'w') as f:
        f.write("Game Status:\n")
        for key, value in game_state.items():
            f.write(f"{key}: {value}\n")

def check_end_conditions():
    if game_state["dayLeftToApply"] <= 0:
        return 999 
    if game_state["health"] <= 0:
        return 998 
    if game_state["motivation"] <= 0:
        return 997
    return None

def get_valid_choice(story_number):
    valid_choices = naratives[story_number]["next"].keys()
    while True:
        try:
            choice = int(input("What is your choice: ").strip())
            if choice in valid_choices:
                return choice
            else:
                print(f"Invalid choice. Please select from {list(valid_choices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def apply_state_changes(story_number, choice):
    if choice in naratives[story_number]["effects"]:
        for key, value in naratives[story_number]["effects"][choice].items():
            game_state[key] += value
    else:
        print("Invalid input")
    return None

def narative(story_number):
    print(naratives[story_number]["text"].format(**game_state))
    choice = get_valid_choice(story_number)
    apply_state_changes(story_number, choice)
    return naratives[story_number]["next"][choice]

def starting_nar():
    print("Because you got married and moved out! You gotta pay bills and provide! Isn't that fun")
    filler = input("Press any button to continue")
    print("Well, you have been applying for jobs, doing school work, and been working, but you got about until april 2025 till you gradduate to find a good paying job!!")
    filler = input("Press any button to continue")
    print("Well, I am glad I am not you, I am just a game! We are going to simulate what it is like applying for any entry level CS Job in 2025. Well Good Luck!")
    filler = input("Press any button to continue")
    print('Becasue you are going to need it...')
    filler = input("Press any button to continue")
    print("Like, for real, I am so glad I am not you right now")
    filler = input("okay... i get it... Press any button to continue")
    print("i mean it though, i am so glad i don't have to apply for jobs")
    filler = input("wow, thanks. Press any button to continue")
    print("am i being annoying")
    filler = input("No or No Press any button to continue")
    print("Thanks! Good luck")
    filler = input("Press any button to continue")


def start_game():
    current_story = 0
    while current_story in naratives:
        print("\n\nGame State: " + str(game_state))
        current_story = narative(current_story)
        end_condition = check_end_conditions()
        if end_condition:
            current_story = end_condition
        
starting_nar()
start_game()
save_game_to_file('game_status.txt')
print("\nYa, you can't get a job now a days, sorry about that")
filler = input("Press any button to continue")
print("\nBut maybe you can try again and see if you can get a job")
filler = input("Press any button to continue")
print("\nHowever, if you look at the game code")
filler = input("Press any button to continue")
print("\nWAIT, DON'T DO THAT")
filler = input("Why")
print("\nI said too much, why i do i have to balber so much")
filler = input("TELL ME WHAT IS IN THE CODE Press any button to continue")
print("\nWell, if you look at the code.../")
filler = input("Press any button to continue")
print("\nYou can tell there is no way a job employeer will reach out")
filler = input("WHAT ress any button to continue")
print("\nYse, it is just a endless loop of applying for jobs with no end in sights")
filler = input("WHY")
print("\nBecuase the programmer didn't have enought time to fully complete this program with other responsibilties going on")
filler = input("Oh.... Press any button to continue")
print("\nAlso, 80 minuites before this assingment is due, (after the beautiful logic of scablitiy was added) he just got a text saying his bestie sister is moving out of state, so he now haves this oppuntinity to complete the assigment as a speed runner would at the end")
filler = input("Oh no, will he complete it in time then? Press any button to continue")
print("\nMaybe, he had to find out a quick way to add more nartiaves since he been so busy he had to put this assingment until the end because he has been applying to jobs in real life")
filler = input("Will he get full points? Press any button to continue")
print("\nI hope so, but given the beautful and wonderful way he made his code to scale dyanmicly and vertically ***something he can now put on his resume btw*** He might get full points")
filler = input("Well, i wish him luck")
print("Quote from mister incredible: Me to kid, me too")