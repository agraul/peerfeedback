# Peer Feedback

`peerfeedback` is a tool that creates pairings for people that give each other feedback. It makes sure that a person is not receiving feedback from a recipient of their own feedback to reduce the likelyhood of biased feedback.


## Requirements

1. Persons to match are identified by their email address
1. Every email address is mapped to two other addresses, twice (once for receiving and once more for providing feedback)
1. Email addresses shall not be matched mutually (if person `A` gives feedback to persons `B` and `C`, then persons `B` and `C` are not allowd to provide feedback to `A`) 
1. Input is done via a MS Office Excel sheet
1. Output is done via a separate MS Office Excel sheet
   1. Output format (each row in sheet): `(candidate)(reciver1)(reciver2)(giver1)(giver2)`
   1. Automatically sent emails


## Algorithm Used

Given persons `A`, `B`, `C`, `D`, `E`, the following pairing will be created. The person that provides feedback is listed on the lefthand side and the feedback targets on the righthand side.

``` text
`A` → `B`, `C`
`B` → `C`, `D`
`C` → `D`, `E`
`D` → `E`, `A`
`E` → `A`, `B`
```

Which can be expressed by this general formula:

``` text
n(0)..n(max-2) → n+1, n+2
n(max-1)       → n(max), n(0)
n(max)         → n(0), n(1)
```

# License

This program was written by Alexander Graul <mail@agraul.de> and is licensed under the GNU General Public License version, either version 3 or (at your option) any later version.
