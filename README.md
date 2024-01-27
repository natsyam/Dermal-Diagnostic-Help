# **Dermal Diagnostic Help**

**Рак кожи** - распространенное злокачественное заболевание, которое часто диагностируется визуально с помощью клинических осмотров и дермоскопического анализа. Набор данных HAM10000, включающий 10 015 дерматоскопических изображений, позволяет разработать автоматизированную систему классификации поражений кожи.

**"Dermal Diagnostic Help"** - приложение, разработанное для помощи в ранней диагностике рака кожи с использованием методов глубокого обучения. Используя датасет HAM10000, этот проект нацелен на создание точной и эффективной модели для классификации кожных образований.

❗️ **Помните, что окончательный диагноз должен ставить только врач.**

![image](https://github.com/natsyam/Dermal-Diagnostic-Help/assets/146081042/087a6735-9a29-4766-8174-b392f590bc2e)

---


Модель фокусируется на обнаружении семи различных классов рака кожи.

**Классы рака кожи:**
- Меланоцитарные невусы (nv)
- Меланома (mel)
- Доброкачественные кератозоподобные образования (bkl)
- Базальноклеточный карцинома (bcc)
- Актинические кератозы (akiec)
- Сосудистые образования (vasc)
- Дерматофиброма (df)

Каждое из заболеваний в HAM10000 датасете имеет свои характерные черты, которые описываются в статье. Вот краткое описание каждого заболевания:

- **nv (Melanocytic nevi):**
Беневольные новообразования меланоцитов, включающие различные варианты. 

- **mel (Melanoma):**
Злокачественное новообразование, происходящее от меланоцитов.
Включает различные варианты меланомы, как инвазивные, так и неинвазивные (in situ). Исключаются не пигментированные, субунгуальные, глазные или слизистые меланомы. 

- **bkl (Benign keratosis):**
Обобщенный класс, включающий себорейные кератозы ("старческие бородавки"), солярные лентиго (плоский вариант себорейных кератозов) и кератозы, похожие на лишай планус (LPLK), которые могут соответствовать себорейному кератозу или солярному лентиго с воспалением и регрессией. Эти подгруппы могут выглядеть по-разному дерматоскопически, но они группируются вместе из-за их схожей биологии и часто отмечаются одним и тем же термином при гистопатологическом исследовании.

- **bcc (Basal cell carcinoma):**
Распространенный вариант эпителиального рака кожи, который редко метастазирует, но разрушает ткани, если не лечить. Появляется в различных морфологических вариантах (плоский, узловой, пигментированный, кистозный и др.). 

- **akiec (Actinic Keratoses and intraepithelial Carcinoma):**
Общие неинвазивные варианты плоскоклеточного рака, которые могут быть вылечены местно без хирургического вмешательства. Некоторые авторы рассматривают их как предшественников плоскоклеточных раков, а не как реальный рак. Оба непрерывно демонстрируют образование корки на поверхности и обычно лишены пигмента.

- **vasc (Vascular skin lesions):**
Сосудистые образования от гемангиом до ангиокератом и пиогенных гранулем.
Включает геморрагии. 

- **df (Dermatofibroma):**
Беневольное кожное образование, рассматриваемое как либо как доброкачественная пролиферация, либо как воспалительная реакция на минимальную травму. Часто коричневого цвета с центральной зоной фиброза дерматоскопически. 

## **Как запустить приложение ?**

```
streamlit run streamlit.py

uvicorn main:app
```

## **Как пользоваться ?**

1. Запустите приложение
2. Нажмите "Загрузить фотографию"
3. После загрузки нажмите "Классифицировать"
4. Модель выдаст предсказание вероятности классов
5. ❗️**Помните, что диагноз должен ставить только квалифицированный врач**

