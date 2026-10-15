# ToothForm: Dental Anatomy 3D — Licensing and model notices

Updated October 15, 2026. This page describes the licensing records for the current ToothForm source and provides all 14 bundled model attribution, license and reuse notices. On October 15 the lower first molars (#19/#30) changed from the Kato and Ohno model to ACTA-DIRECT tooth 0039; build 1.0 (4), prepared on October 14, still contains the earlier Kato model, so the change applies to the next build. The app has not been released on the App Store.

## Application license

ToothForm's original application code is proprietary, © 2026 Sansar Gupta, and is not offered under an open-source license. The planned App Store release is configured to use [Apple's Standard End User License Agreement](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/). Free pricing does not change the software or model license terms.

**Third-party tooth models, scan-derived geometry and other third-party materials retain their own copyrights, applicable licenses and permission requirements. Nothing in this documentation limits rights granted under those licenses.** App-code terms do not replace source terms. Where a source license permits copying, modification or redistribution, recipients retain those rights subject to its conditions, including required attribution and notices of changes.

This page is a documentation clarification, not a custom EULA or an amendment to the agreement selected in App Store Connect. It does not supply missing redistribution permissions or establish compatibility with Store restrictions or technical protection measures. No source author or institution is represented as endorsing ToothForm.

## Current model sources

The current source displays 32 numbered tooth positions and four separate specimen demonstrations from seven source families. Numbers below use the Universal tooth-numbering system. Mirrored counterparts and representative placements do not represent independently scanned specimens.

| Source | Current positions or demos | Published terms and documentation limits |
|---|---|---|
| [Toothnroll — Profico and Augoyard](https://zenodo.org/records/15113184) | #6–11 | The downloaded dataset is published under CC BY 4.0. |
| [Liao et al., 2018](https://doi.org/10.1371/journal.pone.0209698) | #1 and #16 | CC BY 4.0; the source volume is the article's S1 supporting dataset. |
| [ACTA-DIRECT Dataset v2 — Gonzalez Valenzuela / ACTA](https://doi.org/10.48338/VU01-H5ALYJ) | #2/#15, #3/#14, #17/#32, #18/#31, #19/#30 and #21/#28 | The deposit states CC BY 4.0. Tooth class and side were inferred during our morphology review. |
| [Pereira et al., through the OdontoIQ derivative](https://doi.org/10.5281/zenodo.3877625) | Tomo1B, demo 1001 | CC BY 4.0 for the source dataset and the supplied OdontoIQ derivative notice. |
| [Root Canal Anatomy Project — Marco A. Versiani](https://rootcanalanatomy.blogspot.com/2013/06/a-new-microct-based-educational-resource.html) | #4, #5, #12 and #13; demos 1103 and 1108 | Source-specific attributed noncommercial educational terms. No standardized Creative Commons license is asserted; general app redistribution permission is not established by the retained records. |
| [OpenMandible base-model tooth tissues](https://github.com/ArsoVukicevic/OpenMandible) | #20, #22–27 and #29 | No asset license has been established for the base-model STL files. GPLv3 files elsewhere in the source repository do not establish a license for these assets. |
| [Bern / ZMK Tooth Cohort, Tooth007](https://osf.io/rt3da/) | Demo 1107 | The external OSF volume has no dataset license recorded. The associated article's CC BY and data-waiver language has not been confirmed to cover redistribution of this external volume. |

Twenty numbered positions and demo 1001 rest on source data published under CC BY 4.0. The other 12 numbered positions and three demos have noncommercial terms or unresolved redistribution grants in the retained records. Source publication terms and attribution do not independently establish clearance for every form of app distribution.

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) permits reuse, including commercial reuse and adaptation, subject to its conditions. These include preserving required credits and notices, identifying modifications, and respecting recipients' licensed rights. The [full legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en) governs; this summary does not replace it.

## Notices for current source families

Each link opens the complete notice in a readable page with a link to its unchanged plain-text copy. These are attribution, processing and reuse notices; some link to the source license's full legal code rather than reproducing it. They retain the source authors' names, source references, modifications and stated limitations.

- [Toothnroll attribution and processing](DentalMorphology/Resources/Models/TOOTHNROLL_ATTRIBUTION.txt).
- [Liao 2018 attribution and processing](DentalMorphology/Resources/Models/LIAO2018_ATTRIBUTION.txt).
- [ACTA-DIRECT v2 attribution and processing](DentalMorphology/Resources/Models/ACTA_DIRECT_ATTRIBUTION.txt).
- [Scanned-specimen credits, including Tomo1B and the RCAP demos](DentalMorphology/Resources/Models/SCANNED_ATTRIBUTION.txt).
- [OdontoIQ source and derivative license notice](DentalMorphology/Resources/Models/ODONTOIQ_SOURCE_LICENSE.txt).
- [RCAP layered class-representative attribution](DentalMorphology/Resources/Models/RCAP_LAYERED_ATTRIBUTION.txt).
- [RCAP first-premolar attribution](DentalMorphology/Resources/Models/RCAP_PREMOLAR_ATTRIBUTION.txt).
- [OpenMandible attribution and reuse status](DentalMorphology/Resources/Models/OPENMANDIBLE_ATTRIBUTION.txt).
- [Bern Tooth007 attribution and reuse status](DentalMorphology/Resources/Models/BERN007_ATTRIBUTION.txt).

## Retained historical and upstream notices

The following five notices are retained with the app for provenance. The current app package contains no Kato, Dundee or BodyParts3D / Dental Scope geometry. Kato surfaces remain in the local model archive; Dundee surfaces remain local fallback and development resources; BodyParts3D / Dental Scope geometry is a retired development family.

- [Kato and Ohno attribution and reuse status](DentalMorphology/Resources/Models/KATO2009_ATTRIBUTION.txt): public research downloads with no confirmed dataset redistribution grant. Their last placement, the three-rooted lower first molar at #19/#30, is in build 1.0 (4) and was replaced in the source on October 15, 2026.
- [University of Dundee surface-model attribution](DentalMorphology/Resources/Models/DUNDEE_ATTRIBUTION.txt): source models are published under CC BY 4.0.
- [BodyParts3D / Dental Scope geometry attribution](DentalMorphology/Resources/Models/ATTRIBUTION.txt): adapted geometry retains [CC BY-SA 2.1 Japan](https://creativecommons.org/licenses/by-sa/2.1/jp/deed.en) terms.
- [Dental Scope upstream credits](DentalMorphology/Resources/Models/DENTAL_SCOPE_CREDITS.txt): the original upstream credits also mention other anatomy, fonts and web libraries. They are preserved as upstream documentation, not as a dependency inventory for ToothForm.
- [Dental Scope upstream software license](DentalMorphology/Resources/Models/DENTAL_SCOPE_LICENSE.txt): MIT covers the upstream software described in that notice, not ToothForm's original application code or the separately licensed model geometry.

## About these notice copies

All 14 plain-text copies preserve the bundled notice bytes. References inside them to repository paths, local research caches or historical processing records are contextual references, not additional hosted downloads. This website publishes notices and licensing documentation; it does not distribute tooth geometry, source scan volumes, textbook content or course-note files.

The app's Sources & credits and About this model views provide further specimen and processing context. For application help, see [ToothForm support](SUPPORT.md). The [privacy policy](PRIVACY_POLICY.md) explains optional external links and support contact.
