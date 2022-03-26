SingleTon:
 - Used for the ConsoleIO Class, Keeps it to one instance. You don't have to create a new Bufferreader, nor pass the IO object through parameters

Template:
 - There are 2 menu interfaces the user can interact with after he picked the option for a survey or test. I used this pattern for Menu, and it's subclasses SurveyMenu and TestMenu. They are very similair so I used template to capture those similarieties.

Builder:
 - Instead of using Factory Method or Abstract Factory to construct either a Survey or Test, I used a builder. Found at SurveyTestCreator, Survey Builder, and it's subclass TestBuilder. This was for the main reason that Surveys and Tests are dynamic and built depending on user input during runtime. 

Strategy:
 - I used strategy to seperate Questions class into many Different Subclasses that range from the type of question we want. It's hard to have used Decorator, since we would need a concrete subclass to finish on.

Iterator:
 - I used Iterator for creating a list of ResponseIterators, This allows different types of arrays to store Responses, while allowing anyclass outside CorrectAnwserSheet to just see them as an Iterator.

Bridge:
 - I used the builder interface for displaying and taking the Survey. The Survey is the Abstraction, and TakingMethods is the Implementor, with Audio and Visual being the ConcreteImplementors. I used this to allow the interaction to Survey (and it's subclass) to be independent from it
Note: The fuctionality never called for Audio, and yes I recognize, this is just showing that it would beable to handle audio and other methods of displaying and taking if requirment needed to arise