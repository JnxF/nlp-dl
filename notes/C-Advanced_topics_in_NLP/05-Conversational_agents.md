# Conversational agents

AKA Dialog agents forms:
* Phone-based: SIRI, Cortana, Google Now
* Talking to your car
* Communicating with robots
* Mental health
* Chatting for fun

Two classes:
* Goal-based
* Chatbots

Architectures:
* Finite-State: good for passwords or credit cards.
* Active ontology / frame based.

Finite-state dialog:
* It is always the system that controls the conversation.
* Ignored anything the user says that it is not planned.

Dialogue initiative:
* Initiative: who has control of conversation.
* Normal human-human dialogue: initiative shifts back and forth.

System initiative.
* Good: simple to build, user/system always know what they/the user can say next.
* Bad: too limited.

Problems with system initiative:
* Too robotic.
* People solving more than one question in a sentence.

Single initiative + universals:
* Examples: correct is going back one step.
* Start over goes back to the beginning.

Mixed initiative:
* Having a frame with different slots. E.g. _What city are you flying from_, etc.
* User can answer multiple questions at once.

Ontology:
* Way to model

Chatbots:
* Eliza — Pattern-action rules.
* Parry — Adds mental model.

Eliza uses atterns:
* _X_ you _Y_ ME → what makes you think I _Y_ you.
* Examine each word, return the word with highest keyword rank.
* If w exist, check every rule in ranked order.
* Choose the first one that matches and apply transform.
* If no keyword apply, reply "What makes you think that?"

Memory:
* Collection of things the user has said.
* Short term

Eliza:
* Rules that refer to classes of words.
* People deeply emotionally involved.

Parry:
* Same pattern-matching structure as Eliza
* Combines with language understanding

Seq2seq model:
* Using context hidden state
* Decode initial hidden state