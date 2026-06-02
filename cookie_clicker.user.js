// ==UserScript==
// @name         Cookie Clicker Automation
// @namespace    https://github.com/Felipe-Alcantara/Cookie-counter-automation
// @version      1.0.0
// @description  Auto-clicks the big cookie and buys the cheapest available upgrade and product.
// @author       Felipe Martin
// @match        https://orteil.dashnet.org/cookieclicker/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=dashnet.org
// @grant        none
// ==/UserScript==

// Userscript for automating Cookie Clicker. Use with a userscript manager
// such as Tampermonkey. See README for setup.

(function () {
    "use strict";

    // How often the main loop runs, in milliseconds. 1ms freezes the browser;
    // ~200ms keeps clicking fast while staying responsive.
    const LOOP_INTERVAL_MS = 200;

    // Click the big cookie using the game's built-in method.
    function clickCookie() {
        Game.ClickCookie();
    }

    // Parse a localized price string ("1,234" / "1.234") into a number.
    // Returns NaN when the text has no usable digits.
    function parsePrice(text) {
        const digits = text.replace(/[^\d]/g, "");
        return digits ? parseInt(digits, 10) : NaN;
    }

    // Buy the cheapest available product (building).
    function buyCheapestItem() {
        const items = Array.from(
            document.querySelectorAll(".product.unlocked.enabled")
        )
            .map((element) => ({
                element,
                price: parsePrice(element.querySelector(".price").textContent),
            }))
            .filter((item) => !Number.isNaN(item.price))
            .sort((a, b) => a.price - b.price); // ascending: cheapest first

        const cheapest = items[0]?.element;
        if (cheapest) {
            cheapest.click();
            console.log(
                "buy item: " +
                    cheapest.querySelector(".title.productName").textContent
            );
        }
    }

    // Buy the cheapest available upgrade.
    function buyCheapestUpgrade() {
        const upgrades = Array.from(
            document.querySelectorAll("#upgrades .upgrade.enabled")
        )
            .map((element) => {
                // Hover to populate the tooltip that holds the price.
                element.onmouseover();
                const priceEl = document
                    .querySelector("#tooltip")
                    ?.querySelector(".price");
                return {
                    element,
                    price: priceEl ? parsePrice(priceEl.textContent) : NaN,
                };
            })
            .filter((item) => !Number.isNaN(item.price))
            .sort((a, b) => a.price - b.price); // ascending: cheapest first

        const cheapest = upgrades[0]?.element;
        if (cheapest) {
            cheapest.click();
            console.log("buy upgrade");
        }
    }

    function mainLoop() {
        clickCookie();
        buyCheapestUpgrade();
        buyCheapestItem();
    }

    setInterval(mainLoop, LOOP_INTERVAL_MS);
})();
