import requests
import time
import random

# API Configuration
URL = "https://api.hyperbolic.xyz/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}

# List of 100 unique questions
questions = [
    "A futuristic cityscape at night with flying cars",
    "A medieval castle on a mountain during sunset",
    "A cyberpunk street scene with neon lights and rain",
    "A magical forest glowing with bioluminescent plants",
    "A cozy cabin in the snowy woods with smoke rising",
    "A spaceship landing on an alien planet",
    "An underwater coral reef teeming with fish",
    "A steampunk airship flying over Victorian London",
    "A dragon flying over a fiery volcano",
    "A serene Japanese garden in the springtime",
    "A fantasy landscape with floating islands",
    "A haunted house under a full moon",
    "A majestic lion standing on a savanna at dusk",
    "A peaceful beach at sunrise with palm trees",
    "A vintage diner on Route 66 at night",
    "A girl riding a bicycle through a sunflower field",
    "A wizard casting a spell in an ancient library",
    "A robot playing chess with a human",
    "A galaxy with swirling stars and planets",
    "A fairytale castle in the clouds",
    "A futuristic soldier in high-tech armor",
    "A mystical mountain temple surrounded by fog",
    "A wolf howling under the Northern Lights",
    "A market in Marrakech full of colors and spices",
    "A cozy reading nook by a rainy window",
    "A beautiful alien landscape with two suns",
    "A train passing through snowy mountains",
    "A retro 1980s computer setup with neon lights",
    "A fantasy elf archer in a forest",
    "A neon-lit samurai standing in the rain",
    "A pirate ship battling a sea monster",
    "A surreal dreamscape with melting clocks",
    "A cute cat astronaut floating in space",
    "A magical potion brewing in a cauldron",
    "A detailed close-up of a butterfly on a flower",
    "A massive treehouse village in a jungle",
    "A ballerina dancing in a moonlit theater",
    "A knight fighting a dragon in a canyon",
    "A peaceful countryside cottage with flowers",
    "A glowing crystal cave underground",
    "A mountain lake reflecting the stars",
    "A fantasy tavern full of strange creatures",
    "A scene inside a futuristic control room",
    "A spaceship interior with neon lighting",
    "A wolf running through a snowy forest",
    "A fantasy gate glowing with magic",
    "A sci-fi laboratory with floating holograms",
    "A floating castle in the sky",
    "A polar bear family on an iceberg",
    "A forest path covered in autumn leaves",
    "A desert caravan under a starry sky",
    "A jungle temple covered in vines",
    "A stormy sea with crashing waves",
    "A dreamy cloud kingdom with rainbows",
    "A ninja leaping between rooftops at night",
    "A futuristic motorcycle race in a tunnel",
    "A samurai meditating in a bamboo grove",
    "A bustling alien city at night",
    "A peaceful lake with ducks and lilies",
    "A mountain village in the Swiss Alps",
    "A magical deer glowing in the forest",
    "A dragon curled around a treasure hoard",
    "A cat lounging in a cozy café",
    "A space station orbiting Earth",
    "A haunted forest with glowing eyes",
    "A phoenix rising from the ashes",
    "A retro arcade with pixel games",
    "A girl painting in a field of tulips",
    "A futuristic skyline at dusk",
    "A Viking ship in icy waters",
    "A tiger walking through a jungle mist",
    "A fantasy map on a wooden table",
    "A steampunk workshop full of gadgets",
    "A tree made of glowing crystals",
    "A cute dog wearing astronaut gear",
    "A cybernetic human in a neon city",
    "A magical underwater city",
    "A gnome garden with tiny houses",
    "A rustic bakery with fresh bread",
    "A mountain range during golden hour",
    "A glowing orb floating in a temple",
    "A fox sleeping in a bed of flowers",
    "A fairy playing with fireflies",
    "A sci-fi tank rolling through a desert",
    "A giant robot walking through a city",
    "A peaceful moonlit beach",
    "A fantasy battle between light and dark",
    "A lush green valley with waterfalls",
    "A panda eating bamboo in the forest",
    "A time traveler stepping out of a portal",
    "A magical street market at night",
    "A knight riding a white horse",
    "A gothic cathedral under stormy skies",
    "A giant octopus in a sunken ship",
    "A tropical island paradise",
    "A magical mirror showing alternate worlds",
    "A deep space black hole",
    "A high-tech drone flying over mountains",
    "A spaceship chase through asteroid fields",
    "A charming village during a festival",
    "A robotic cat exploring a ruined world",
    "A windmill on a sunny Dutch farm",
    "A magical staircase in the clouds"
]

# Verify we have 100 questions
print(f"Total questions loaded: {len(questions)}")

# Function to send API request
def send_chat_request(question):
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "stability-ai/sdxl-turbo",
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# Main bot loop
def run_chat_bot():
    print("Starting automated chat bot...")
    available_questions = questions.copy()  # Work with a copy to preserve original list
    
    for i in range(100):  # Fixed to 100 since we have exactly 100 questions
        if not available_questions:
            print("Ran out of questions unexpectedly!")
            break
        
        # Pick and remove a random question to avoid repetition
        question = random.choice(available_questions)
        available_questions.remove(question)
        
        # Send request and print results
        print(f"\nQuestion {i + 1}: {question}")
        answer = send_chat_request(question)
        print(f"Answer: {answer}")
        
        # Random delay between 1-2 minutes (60-120 seconds)
        delay = random.uniform(60, 120)
        print(f"Waiting {delay:.1f} seconds before next question...")
        time.sleep(delay)
    
    print("\nCompleted 100 questions!")

# Run the bot
if __name__ == "__main__":
    run_chat_bot()