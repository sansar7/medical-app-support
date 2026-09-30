# DentalFaceScan Support

DentalFaceScan is an iPhone-only face and object capture app. The current application target requires iOS 27. Camera, TrueDepth, rear LiDAR and Object Capture availability depend on the physical iPhone and selected method. Simulator samples exercise software only. Clinical accuracy and actual exocad interoperability require independent validation; facial capture does not replace an intraoral scanner.

## Languages

The bundled interface supports English, Spanish, French, German, Italian, Brazilian Portuguese, Simplified Chinese, Traditional Chinese, Japanese, Korean, Hindi, Arabic, Indonesian, Turkish, and Vietnamese. Russian is not bundled. Substantial clinical, capture, safety and privacy guidance intentionally remains in English while translation review is pending. This includes many public guide passages, even when navigation and selected instructions appear in your preferred language. English is the primary language; translations may be inaccurate. The **Privacy and storage** view includes this notice. The app follows your system’s preferred supported language or the standard per-app language setting, then falls back to English when no supported preference is available. Relaunch after changing the language. Brazilian Portuguese uses `pt-BR`; Traditional and Simplified Chinese have separate resources.

Translations are included with the app and work offline. There is no translation account, translation permission, model download, or runtime translation service. Changing the interface language does not translate patient-entered text, saved names, custom labels, or imported records. Arabic uses the system’s right-to-left layout. Technical identifiers, file formats, units, and stored data contracts retain their original meanings.

When reporting a language or layout problem, include the app version, platform, interface language, text size, and the exact label or view. Use fictional data in screenshots. Spoken Siri availability and recognition depend on Apple’s supported languages and device settings.

## Contact

Contact Sansar Gupta at [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com). Include the app version/build, iPhone model, iOS version, selected capture method, interface language and steps to reproduce. Do not include patient names, identifying case labels, facial images, scan models, or clinical records in ordinary email or public issues.

## Capture and review

Open **New scan**, choose a capture method, and follow its device-specific guidance. Obtain informed consent. Keep the subject and facial/jaw position still, use diffuse even lighting, and move the phone as directed. Use a non-identifying case label; a facial model can itself identify a patient.

For a stalled capture, open **Capture diagnostics → Share diagnostic report** before restarting. You review and choose the destination in the system share sheet. The diagnostic report contains timing, readiness and processing state, without photographs, models, case labels or file paths. It is not sent automatically.

Gaussian appearance and independently measured depth geometry are separate representations. Object mode produces a visual Gaussian splat without a CAD surface. Inspect coverage, holes, orientation and known physical dimensions independently before using any facial geometry in a CAD workflow.

## Storage, export and deletion

Scans are saved in private, protected on-device storage. The app has no patient account, cloud reconstruction service or automatic upload. Gaussian captures retain their source photographs and calibrated camera poses locally. Ordinary Gaussian and CAD exports omit the retained source photograph dataset, but photographic textures and facial geometry in exported models can identify a person.

Open a saved scan, choose an available export format, and choose a destination in the share sheet. CAD mesh exports use millimetres; Gaussian splat coordinates use metres. Verify the receiving application’s units and anatomical left/right orientation. Formats do not enforce units.

Open a scan, choose **Scan actions → Delete scan**, and confirm to remove its saved model and capture data. Copies already exported to Files, other apps or recipients must be removed separately. Private scan storage is excluded from system backups; export the needed files before removing the app. The developer cannot recover locally lost scans.

## Privacy

Read the in-app **Privacy and storage** view and the [privacy policy](PRIVACY_POLICY.md). Only public capture guides are exposed to Siri and Spotlight. Patient scans, case labels, images and geometry are excluded. Language resources are bundled; private scan content is never submitted to a translation service.
