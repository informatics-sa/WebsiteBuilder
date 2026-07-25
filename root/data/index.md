---
lang: en
title: Public Data API
layout: default
---
# Public Data API
WebsiteBuiler: {{ site.data.settings.resolved_builder }}

## How to read documentation
this document is a description of a series of json files, every field is defined as `name: `[`Type`](#data-types)`, <general description> `[`<optional set of properties>`](#properties). any reference to the keyword `self` in the description should be interpretted as the value of the field defined in the file by the user.

### Data types
#### JSON datatypes
- String
- Integer
- Boolean
- Float
- Array: JSON array `[...]`
- Dictionary/Object: JSON object `{...}`

#### Custom defined
<details markdown="block">
<summary>Emum: MetaType</summary>

A MetaType is the underlying Type of some custom defined Type, for example, `Date` is Type with `String` being its MetaType, but with the additional semantics that it's a `String` that holds an ISO 8601 formatted `Date`.

`Enum` is a MetaType, that is used to describe other types which are effectively an enum. it's followed by a set of cases, a `case` has a `name` and a `type`, which is described like other fields. Later in some file, when a field (F) has a type (T), such that T has `Enum` as its MetaType, F's type is effectively the `type` of **one** of the cases. (note: each case has `name` and `type`, but only `type` is relevent to the actual data files, `name` is only used for documention purposes. more details on this in the example bellow)

For example, we can define a Type `Image` that has the MetaType `Enum`. with cases:
- case `remote`: Dictionary, containing:
  - `url`: URL, referencing some image on the web.
- case `local`: Dictionary, containing:
  - `file_path`: String, relative filepath from `/img` folder.

Later we can have a field use this Type as follows:
- `logo`: Image, logo used in navbar of website.

This field, `logo`, can **either** be of the type declared by `Image:url` **or** `Image:local` (also note this is how we can refer to cases by their `name` in documentation. we can also refer to cases of certain fields, for example `logo:url` or `logo:local`).
valid examples:
```json
logo: {
    url: "https://example.com/image.png"
}
```
**or**
```json
logo: {
    file_path: "./image.png"
}
```
Note that having both `url` and `file_path` in one Dictionary will result in an error.

We can also have a shorthand syntax for "initializing" Types with `Enum` MetaType for use in documentation, the syntax is `T:C(V)` for a Type `T` with MetaType `Enum`, and case `C`, and value `V`. For example, if we want to document that it's forbidden to set `logo` to a local image called "forbidden.png", we can say:
"it's not allowed for `logo` to be `Image:local({file_path: "./forbidden.png"})`".

---
</details>

- Date: String, gregorian date in[ ](https://xkcd.com/1179/)[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`yyyy-mm-dd`)
- URL: String, starts with prefix `https://` and without suffix `/` except when required
- Email: String, an email
- BuilderVersion: Enum
  - case `release`: Dictionary, containing:
    - `version`: String, version number in the [Semantic Versioning](https://semver.org) format, minimum version of [WebsiteBuilder](https://github.com/informatics-sa/WebsiteBuilder) required to successfully build the website.
    - `nightly`: Boolean, whether or not to consider nightly releases of WebsiteBuilder (prerelease). default is `false`, unless `version` is refering to a prerelease, in which case `true` will be the default. **(optional)**
  - case `branch`: Dictionary, containing:
    - `branch`: String, will fetch WebsiteBuilder from this branch.
  - case `commit`: Dictionary, containing:
    - `commit`: String, will fetch WebsiteBuilder from this exact commit.

### Properties
By default each property is required, here are the additional properties:
- **unique**: It should be distinct through the whole file
- **optional**: It's not required, the default value is `null` except if mentioned otherwise
- **deprecated**: It was used previously and not removed because of development issues
- **future**: The field isn't used in any current data, but could be useful in the future development

## Settings file
Each repository has its own [`/data/settings.json`](/data/settings.json) which could have these fields:
- `website_builder`: BuilderVersion, this is used by `prebuild.py` to decide which version of WebsiteBuilder is suitable for the website, and fetch it. Default is `BuilderVersion:branch({branch:"main"})` **(optional)**
- `version`: String, this is an alias to `website_builder:release({version: self})`. **(optional, note that either this or `website_builder` can exist, but not both.)**
- `old_id_system`: Boolean, using `id` instead of `iid`. Default false.  **(optional)**
- `codeforces`: Boolean, in case each user has a Codeforces account. Default false. **(optional)**
- `icon`: String, filename of favicon inside `/img` folder. **(optional)**
- `logo`: String, filename of logo inside `/img` folder. Recommended to be SVG. **(optional)**
- `home_image`: String, filename of an image inside `/img`.
- `enable_exams_page`: Boolean, default false
- `enable_members_index`: Boolean, default false
- `enable_image_library`: Boolean, default false

## [`/data/people.json`](/data/people.json)
An array of people, each person has the following:
- `iid`: Integer, informatics ID of the student, currently fetched from IDs assigned by Marko **(unique)**
- `id`: String, lowercase with no spaces ID usually in format `firstname_lastname`, not used anymore and shouldn't be written, it will be removed by devleopers when not needed anymore **(deprecated)**
- `arname`: String, Name in Arabic
- `enname`: String, Name in English
- `level`: Integer, current SIT Level ("`-1`" if he/she graduated, "`-2`" if he/she disqualified/left before graduating, "`-3`" if he/she was never a student)
- `graduation`: Integer, graduation year **(optional)**
- `codeforces`: String, Codeforces username. Used only with `codeforces: true` in `settings.json` **(optional)**
- `email`: Email, most official email, usually `...@sainformatics.org`, used in case of [contact page](https://sainformatics.org/contact) **(optional)**
- `female`: Boolean, used in girls competitions, default is `false` **(optional)**

## [`/data/participations.json`](/data/participations.json)
An array of olympiads SIT participated in, each olympiad has the following:
- `name`: String, An id of an olympiad that exists in `olympiads.json`
- `year`: Integer, year
- `country`: String, the 2-letters country code of the host country of the olympiad.
- `start`: Date, The start day of the olympiad
- `end`: Date, the end day of the olympiad
- `participants`: Dictionary of `<member_id>: <award_name>` of the participants __in SAU order__.
    - `<award name>`: (`gold`/`silver`/`bronze`/`hm`) (null in case of no award)
- `scores`: Dictionary of `<member_id>: <scores_array>` **(optional)**
- `website`: URL, Olympiad website of that specific year **(nullable)**
- `online`: Boolean, indicates if Saudi participated online or not, default is False **(optional)**

## [`/data/olympiads.json`](/data/olympiads.json)
An array of olympiads SIT participated in, each olympiad has the following:
- `id`: String, Should be lowercase, 3/4-letters short olympiad name (i.e. `ioi`, `imo`, `egoi`) **(unique)**
- `arname`: String, Full name in Arabic
- `enname`: String, Full name in English
- `official`: Boolean, is Saudi Arabia an official country or not
- `participations_count`: Integer, How many students participate per year needed when it's used in `tsts.json`. **(optional)**
- `website`: URL, General Olympiad website, shouldn't be a specific year website except if it was the first version of the olympiad **(nullable)**

## [`/data/images.json`](/data/images.json)
These images would be shown in [Image libary](https://sainformatics.org/images), shouldn't have a strict rules about the title/description.

You might check and share [image proposals form](https://forms.gle/oxJKdEX78kA8fYzQ6), which is maintained by the website developers.

An array of images, each image consist of these labels:
- `src`: String, Filename of the image in [`/img` directory in the repository](https://github.com/informatics-sa/Website/tree/main/root/img) 
- `artitle`: String, Arabic title
- `entitle`: String, English title
- `ardescription`: String, Arabic description
- `endescription`: String, English description
- `date`: Date, the date of this image

## [`/data/contact.json`](/data/contact.json)
A dictionary of (`developers`/`maintainers`/`admin`), each having an array of person ID

## [`/data/exams.json`](/data/exams.json)
A dictionary of exam IDs, where every exam has:
- `name`: String, Name of exam in English
- `date`: Date, The day of the exam
- `problems`: Array of problem ID
- `participants`: Dictionary of student ID and an array of floats which is score per task

## [`/data/tsts.json`](/data/tsts.json)
A dictionary of year and olympiad IDs, and every olympiad ID contains:
- `exams`: An array of exam IDs, or a dictionary in case of different weights
- `min_birthdate`: Date, minimum eligable birthdate for participants, works only in Informatics currently (Optional)
- `female_only`: Boolean, True if only female is eligable for this olympiad, default false (Optional)
- `execluded`: Array of student ID, members who are execluded from the page
- `participants_count`: Integer, count of participants, default is taken from `olympiads.json` file (Optional)
```json
{
    "2025": {
        "_general_excluded": ["sultan_alaiban"],
        "ioi": {
            "exams": ["exam1", "exam2"],
            "min_birthdate": "2009-06-30",
            "female_only": false,
            "excluded": ["muaath_alqarni", "ali_alsalman"]
        }
    }
}
```
additionally, if the TSTs for a certain olympiad is weighted, you can use a dictionary of exam ID to weight instead of an array in the `exams` field. for example:
```json
{
    "2026": {
        "ioi": {
            "exams": {
                "exam1": 0.2,
                "exam2": 0.4,
                "exam3": 0.4
            }
        }
    }
}
```

Additional rules (Optional):
- `excluded`: Array, of strings student ID
- `min_graduation`: Integer, minimum graduation year to be eligable
- `female_only`: Boolean, true if the competition is female only
- `min_birthdate`: Date, the minimum birthdate for eligibility


# Constant files
These files are needed, but they aren't database kind.
## [`/data/countries.json`](/data/countries.json)
## [`/data/translations.json`](/data/translations.json)
