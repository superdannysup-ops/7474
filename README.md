# HangulCraft — 한국어 모험 (Korean Survival)

**An original Minecraft Java Edition Fabric mod project** that turns survival gameplay into a practical beginner-to-intermediate Korean language course. Learn the Korean word for a block while mining it, meet an animal and learn its name when you defeat it, identify your tools in Korean, and practice with clickable chat quizzes. Get XP and emerald rewards for studying.

> **Version:** Minecraft Java **1.21.1** · **Fabric** · **Java 21** · 1.0.0
>
> **Project status:** Complete editable source project. It has **not** been compiled against Minecraft libraries or tested in-game in this delivery environment. Build it using Gradle or GitHub Actions (below) to get the actual mod JAR. This is not a prebuilt installation file.

## What you can do

- **Learn naturally:** Break stone, gather wood, hold a sword or pickaxe, and get Korean words during survival.
- **Learn mobs:** Defeat mobs and learn their Korean names. (Doesn't interfere with normal mob drops.)
- **163 vocabulary words:** Objects, blocks, tools, food, farming, mobs, places, and survival concepts (A1/A2).
- **25 grammar quizzes:** Korean survival sentences using particles, location markers, noun modifiers, past and future tense, `-고`, `-지만`, `-(으)려고`, `-고 있어요`, comparisons, and more.
- **Clickable multiple-choice questions:** Click `[1]`–`[4]` in chat, or type the command. Explanation appears *after* answering.
- **In-world mining challenges:** A context-specific quiz appears after you mine 12 recognized blocks (if you aren't already answering a quiz).
- **Beginner and immersion modes:** In immersion mode, word discovery messages hide pronunciation and English; quiz choices remain in English so you can answer.
- **Daily reward:** Answer 5 questions correctly to receive **2 emeralds + 30 XP** once each server-local calendar day. Correct answers also give 5 XP; discovering a new word gives 1 XP.
- **Practice what you struggle with:** Weak vocabulary is weighted more frequently in regular quizzes and review chooses low-mastery *discovered* words.
- **Persistent progress:** World-local `hangulcraft-progress.json`, separated by player UUID, saved on progress updates and shutdown.
- **Multiplayer compatible:** Runs on the server for all players; for single-player, install it in your local Fabric client.

## Getting the JAR — easiest: GitHub Actions

1. Extract this project ZIP. Create a GitHub repository and upload/commit **everything inside** the `HangulCraft` folder to the **repository root**, including the hidden `.github/workflows/build.yml` file. Do not upload the ZIP alone or make `HangulCraft` a folder inside the repository.
2. In GitHub, open **Actions → Build HangulCraft JAR → Run workflow → Run workflow**. You can also push a commit to run it automatically. The manual button is available after the workflow exists on your default branch.
3. Open the completed run and download **Artifacts → HangulCraft-Minecraft-1.21.1**.
4. Extract the downloaded artifact ZIP to get the built `hangulcraft-1.0.0.jar`. If the job fails, open the **Build Fabric JAR** step for the compiler error; no JAR is produced on failure.

A free GitHub account can run the included workflow under its normal available quota. The workflow downloads Gradle, Minecraft development dependencies, and builds the mod with Java 21. GitHub workflow permissions and availability can vary.

## Build on your computer instead

Requirements: Java 21 JDK, internet access, **Gradle 8.12.1**, Minecraft development dependencies fetched by Gradle.

In a terminal inside this project folder:

```bash
gradle build
```

Or open the project in **IntelliJ IDEA** as a Gradle project and run the `build` task. The output, **if the build succeeds**, will be:

```text
build/libs/hangulcraft-1.0.0.jar
```

Because the project does not bundle Gradle itself, `gradlew` is not included; use `gradle` on your computer or the GitHub build workflow.

## Install after building

1. Launch the Minecraft Launcher with Java Edition **1.21.1**.
2. Install [Fabric Loader](https://fabricmc.net/use/installer/) for Minecraft 1.21.1.
3. Download [Fabric API](https://modrinth.com/mod/fabric-api) **for 1.21.1**.
4. Put both `fabric-api` JAR and the **built** `hangulcraft-1.0.0.jar` in your Minecraft `mods` folder. On Windows, it is usually `%appdata%\.minecraft\mods`.
5. Start the **Fabric 1.21.1** profile and open or create a world. A greeting appears in chat.
6. Type `/korean start` for a short tutorial and your first interactive question.

This is a **Fabric mod**, not a Forge / NeoForge / Bedrock mod. If playing on a dedicated server, install it and Fabric API on the server; clients don't need it, because the mod uses commands and vanilla chat.

## In-game commands

| Command | What it does |
|---|---|
| `/korean` | Clickable main menu |
| `/korean start` | Mini-lesson + first quiz |
| `/korean quiz` | Mixed vocabulary and grammar questions |
| `/korean quiz vocab` | Vocabulary-only quiz |
| `/korean quiz grammar` | Grammar-only quiz |
| `/korean quiz review` | Quiz less-mastered discovered words |
| `/korean answer 1`–`4` | Submit your answer (or click one) |
| `/korean vocab` | Review latest 12 discovered words and mastery |
| `/korean daily` | Today's 5-question challenge |
| `/korean stats` | View learning stats and streaks |
| `/korean mode beginner` | Korean + English/romanization on discovery |
| `/korean mode immersion` | Korean-only discovery popups |
| `/korean level a1` | Starter vocabulary / grammar |
| `/korean level a2` | Unlock both A1 and A2 content |

### A quick gameplay example

1. Punch a tree. Chat shows `새 단어! 나무` (new word: wood) with Korean example `나무가 필요해요.`
2. Grab a stone pickaxe. Chat shows `곡괭이` with `곡괭이로 돌을 캐요.`
3. Mine 12 stone/wood blocks: a click-to-answer quiz pops up: `무슨 뜻이에요? 돌`.
4. Click the English meaning `stone`. Chat shows `정답이에요!` (Correct!), with the pronunciation and example sentence, and gives 5 XP.
5. Solve 5 correct quizzes in a day to receive emeralds and extra XP.

## How to change or add lessons

Editable lesson data lives here:

```text
src/main/resources/data/hangulcraft/vocabulary.json
src/main/resources/data/hangulcraft/grammar.json
```

Each vocabulary entry has a unique `id`, Korean `ko`, English `en`, pronunciation, a Korean/English example, a CEFR-inspired `level` (A1/A2), a category, and trigger identifiers such as `minecraft:stone`. These levels are **learning difficulty labels, not an official TOPIK classification**. A vocabulary item without game triggers still appears in quizzes. Mob entries use entity IDs like `minecraft:zombie`. Edit UTF-8 JSON, rebuild, and restart Minecraft.

## How the files are organized

```text
HangulCraft/
  src/main/java/com/hangulcraft/
    HangulCraftMod.java    # Fabric entrypoint, commands, world events, rewards
    LessonBook.java       # lesson loading / lookup
    QuizEngine.java       # clickable questions, spaced review weighting
    PlayerProgress.java   # player stats and mastery
    ProgressStore.java    # world save/load
  src/main/resources/
    fabric.mod.json
    data/hangulcraft/vocabulary.json
    data/hangulcraft/grammar.json
  .github/workflows/build.yml  # automatic JAR build
  build.gradle, settings.gradle, gradle.properties
```

## Notes / known limitations

- Quizzes use **text**, not native-speaker audio or a full-screen GUI. Korean pronunciation is provided in text form on discoveries in beginner mode and after questions.
- The mod doesn't replace Minecraft's entire UI language or enforce Korean-only world gameplay. It's a learning layer added to survival.
- The A1/A2 level tags are approximate and vocabulary translations simplify some context-dependent Korean words.
- New vocabulary notifications happen on first encounter; replay discovered vocabulary via `/korean vocab` or quizzes.
- The daily quest follows the **server's local date**.
- No compiled binary is included: build verification requires Minecraft dependencies that couldn't be downloaded in the creation environment.
- Back up your worlds before adding new mods. To preserve progress between installs, retain the world's `hangulcraft-progress.json` file.

Built against version conventions and APIs described in [Fabric documentation](https://docs.fabricmc.net/) and [Fabric's 1.21.1 guide](https://fabricmc.net/2024/05/31/121.html).
