# Todo
### Relatively ez (I have an idea what I;m doing)
* Create a base AI interface for the plane (AIBase), with abstract methods for plane control
* Create some neural nets/perceptrons/whatever inheriting from AIBase, implementing the plane control methods
### Never really did that before
* Create some kind of matchmaking/game controller/evolution controller
    * Given a network population with X nets (plane pilots)
    * Let each pilot fight with every other one
    * Give pilots points for winning (example formula: 1 point every frame being alive, and 150% bonus for winning the fight)
        * Example: pilot A fights with pilot B for 200 frames
        * A wins
        * A gets 200 * 150% = 300 points
        * B gets 200 points
    * When every pilot has tried beating every other pilot, best one will be chosen
    * Next generation of networks will emerge from the best pilot
        * Proposal - network breeding:
            * 50% of the next population keeps 90% of parent's genes
            * 25% gets 80% of genes
            * 15% gets 70% of genes
            * 10 % gets 60% of genes
        * That would make evolution pretty dynamic and fun to watch, I guess
* Implement gamestates:
    * AI training - just nets fighting each other
    * Skynet mode (i couldn't resist) - let the best AI pilot from current generation fight with a human player
* Some key shortcuts to switch between modes and... do things..? (like saving current nets data, generate fancy plots etc)
* Fancy UI, for no real reason
