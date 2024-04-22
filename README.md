**Test case:**
step 1 : go to website : https://orteil.dashnet.org/cookieclicker/
step 2: counte the number of taps on cookies


Screenshots : 
![image](https://github.com/RiddhiGondaliya/Cookie-counter-automation/assets/42887563/2206f6ae-9f8d-46cb-81b2-d233c75855fd)


![image](https://github.com/RiddhiGondaliya/Cookie-counter-automation/assets/42887563/6ca54500-7026-42dc-a351-ea93185d43d8)

https://github.com/RiddhiGondaliya/Cookie-counter-automation/assets/42887563/8a5bc312-7e07-47c5-87e0-e597eab7d78b

---

## Repository Update Overview

In this repository update, the following changes were made:

I have revised and updated Riddhi Gondaliya’s original code, as her version was not functioning correctly on my system. After acquiring the Chrome driver and implementing some adjustments to the code, I encountered two primary issues:

1. **Manual Data Saving:** The script failed to automatically save progress upon each session start, necessitating manual data saving.
2. **Suboptimal Click Speed:** The click speed was deemed too slow and inefficient for effective gameplay, prompting the exploration of alternative solutions.

Instead of creating a standalone Python file to initiate the browser and perform clicks, I opted to delve into the site's code itself and developed a script within it using Tampermonkey. This approach allows for actions on the site that are universally compatible across different browsers.

## Python Version

**Original Script Overview:**
1. Utilizes Selenium to automate the Cookie Clicker game.
2. Performs clicks on the cookie and attempts to purchase the cheapest available product.
3. Lacks functionality for saving game progress.
4. Does not support pausing or resuming script execution.

**Enhanced Script Features:**
1. Utilizes Selenium for game automation.
2. Introduces additional functionalities:
    - Retrieves the current cookie count.
    - Facilitates product purchases.
3. Implements functionality to load cookies from previous sessions for progress continuity.
4. Supports pausing and resuming script execution via the 'p' and 'r' keys, respectively.
5. Incorporates the keyboard module for key press detection.
6. Offers various enhancements over the original script:
    - Implements saving and loading of game progress.
    - Enables pausing and resuming of script execution.
    - Adopts a more organized code structure with distinct functions for different tasks.
    - Enhances code readability and maintainability.

## JavaScript Version

**Script Objective:**
- Automated gameplay for Cookie Clicker.
- Compatible with userscript managers such as Tampermonkey.

**Functionality Overview:**
1. **clickCookie():**
   - Action: Clicks the cookie within the game.
   - Implementation: Utilizes the game's built-in method (`Game.ClickCookie()`).

2. **buyCheapestItem():**
   - Action: Purchases the cheapest available item.
   - Implementation:
     - Retrieves unlocked and enabled items.
     - Maps elements to an array with their corresponding prices.
     - Sorts items by price in descending order.
     - Buys the cheapest item by clicking on it.
     - Logs the purchase.

3. **buyCheapestUpgrade():**
   - Action: Acquires the cheapest available upgrade.
   - Implementation:
     - Retrieves enabled upgrades.
     - Maps elements to an array with their corresponding prices.
     - Triggers the mouseover event to display the price tooltip.
     - Sorts upgrades by price in ascending order.
     - Buys the cheapest upgrade by clicking on it.
     - Logs the purchase.

**Main Loop Execution:**
- Function: `mainLoop()`
- Action: Initiates the primary loop of the script.
- Components:
  - Clicking the cookie.
  - Purchasing the cheapest upgrade.
  - Purchasing the cheapest item.

**Execution Frequency:**
- The main loop is activated using `setInterval(mainLoop, 1)`, executing every 1 millisecond.

--- 