# Чек-лист узгодженого профілю — Tetiana Kotolup

Мета: одне й те саме ім'я, заголовок і опис на всіх майданчиках. Це те, що в SEO/GEO називають NAP-консистентністю (Name-Address-Position) — і Google, і AI-моделі довіряють більше, коли незалежні джерела повторюють одну й ту саму інформацію.

## Єдина формула (копіювати всюди однаково)

**Заголовок:** AI Automation Developer — n8n, OpenAI GPT-4o, Anthropic Claude

**Короткий опис (About/Bio, 1 версія на всі майданчики):**
> AI Automation Developer building n8n workflows, AI voice agents, Telegram AI bots, and full-stack AI SaaS products with OpenAI GPT-4o, Anthropic Claude, Node.js, TypeScript, and PostgreSQL. Based in Brno, Czech Republic — working with clients internationally.

**Локація всюди однаково:** Brno, Czech Republic

**Фото:** те саме, що на сайті (`foto.jpeg`)

**Портфоліо-посилання, яке додаєш всюди:** https://tetianakotolup.com/

---

## Майданчики

- [ ] **LinkedIn** — заголовок профілю, About-секція з формулою вище, посилання на сайт у "Featured" і в контактах. Регулярні пости про кейси (GrowthLab AI, WealthMirror AI, AI CRM) підвищують частоту, з якою AI-моделі бачать і цитують профіль.
- [ ] **Djinni.co** — звірити, що опис і заголовок збігаються з сайтом дослівно.
- [ ] **GitHub (профіль tetiana-a)** — додати bio з тією ж формулою + посилання на tetianakotolup.com і LinkedIn. Створити профільний README.md з ключовими словами (n8n developer, AI automation Czech Republic).
- [ ] **Upwork / Freelancer.com** — якщо плануєш брати проекти з фрілансу, той самий заголовок і опис.
- [ ] **Clutch.co** — актуально, якщо позиціонуєш себе як підрядника для бізнесу (B2B-запити типу "AI automation agency").
- [ ] **Malt.cz / Navolnenoze.cz** — чеські фріланс-платформи, дають локальну видимість для запитів "AI developer Brno/Czech Republic".
- [ ] **Google Business Profile** — якщо оформиш послуги як OSVČ-бізнес, це підсилює і звичайний, і AI-пошук локальним контекстом.

## Після реєстрації на кожному майданчику

Додай URL профілю в масив `sameAs` у JSON-LD на сайті (файл `index.html`, розділ Structured Data на початку `<head>`). Це прямий машинно-читаний зв'язок між усіма профілями — саме на нього спираються AI-системи, коли перевіряють, що це справді одна й та сама людина.
