# Karami

**Karami** is a WhatsApp-based mini-app that helps Nigerian parents and caregivers of deaf or hard-of-hearing children learn Nigerian Sign Language (NSL) — one sign at a time.

---

## What It Does

Karami sends simple, daily NSL lessons through WhatsApp using:
- Short looping GIFs to show each sign
- One-line text explanations
- Curriculum-based modules (mealtime, hygiene, emotions, etc.)
- Interactive quizzes via WhatsApp
- "Ask-a-Sign" search tool (like a dictionary)
- Progress tracker + printable flashcards (paid plan)

---

## Why It Matters

In Nigeria, many families:
- Can't afford formal sign language classes
- Have limited access to interpreters or schools for the deaf
- Own only basic smartphones with limited internet

Karami solves this by using **WhatsApp**, which they already use, to deliver **free or low-cost** sign language lessons directly to them.

---

## How It Works

- **Frontend**: WhatsApp chatbot interface (using Twilio or Meta API)
- **Backend**: Python or Node.js bot logic
- **Media**: GIFs + text stored in folders by theme (e.g., mealtime)
- **Data**: Lightweight progress tracker (Google Sheets or JSON)

---

## Planned Pilot Metrics

- % of parents who learn 15+ signs in 2 weeks
- % who report better communication with their child
- % who complete 1 full module

---

## Partnerships (Planned)

- Nigerian CODA community
- Deaf education NGOs
- Nigerian Sign Language instructors

---

## Folder Structure
karami/
├── README.md
├── chatbot_flow.txt
├── karami_bot.py
├── media/
│ ├── eat.gif
│ └── thank_you.gif
└── docs/


---

## Team

- Karami

---

## License

MIT License
