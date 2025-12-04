(function () {
    if (typeof document === "undefined") {
        return;
    }
    var root = document.documentElement;
    var lang = root && root.getAttribute("lang") ? root.getAttribute("lang") : "en";
    var label = lang === "tr" ? "Dil sekmeleri" : "Language tabs";
    var sets = document.querySelectorAll(".sd-tab-set");
    if (!sets.length) {
        return;
    }
    sets.forEach(function (set, index) {
        if (!set.getAttribute("aria-label")) {
            set.setAttribute("aria-label", label);
        }
        if (!set.id) {
            set.id = lang + "-tabset-" + (index + 1);
        }
    });
})();
