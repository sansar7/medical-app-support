# Easy3D Capture Support

Easy3D Capture is an iPhone-only face and object capture app. The current application target requires iOS 27. Both Object and Face modes use rear-camera photogrammetry. Availability depends on the physical iPhone supporting native Object Capture and reconstruction; the app checks both capabilities. Front-camera and Gaussian capture are no longer available. Simulator samples exercise software only. Clinical accuracy and actual exocad interoperability require independent validation; facial capture does not replace an intraoral scanner.

## Languages

The bundled interface supports English, Spanish, French, German, Italian, Brazilian Portuguese, Simplified Chinese, Traditional Chinese, Japanese, Korean, Hindi, Arabic, Indonesian, Turkish, and Vietnamese. Russian is not bundled. Substantial clinical, capture, safety and privacy guidance intentionally remains in English while translation review is pending. This includes many public guide passages, even when navigation and selected instructions appear in your preferred language. English is the primary language; translations may be inaccurate. The **Privacy and storage** view includes this notice. The app follows your system’s preferred supported language or the standard per-app language setting, then falls back to English when no supported preference is available. Relaunch after changing the language. Brazilian Portuguese uses `pt-BR`; Traditional and Simplified Chinese have separate resources.

Translations are included with the app and work offline. There is no translation account, translation permission, model download, or runtime translation service. Changing the interface language does not translate patient-entered text, saved names, custom labels, or imported records. Arabic uses the system’s right-to-left layout. Technical identifiers, file formats, units, and stored data contracts retain their original meanings.

When reporting a language or layout problem, include the app version, platform, interface language, text size, and the exact label or view. Use fictional data in screenshots. Spoken Siri availability and recognition depend on Apple’s supported languages and device settings.

## Contact

Contact Sansar Gupta at [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com). Include the app version/build, iPhone model, iOS version, selected subject (Object or Face), interface language and steps to reproduce. Do not include patient names, identifying case labels, facial images, scan models, or clinical records in ordinary email or public issues.

## Capture and review

Open **New scan**, choose **Object** or **Face**, and follow the rear-camera guidance. Keep the subject stationary, use diffuse even lighting, and capture overlapping views. For an object, move around its accessible sides and include higher/lower angles. For a face, obtain informed consent, hold the chosen facial/jaw position still, and follow the front and side facial arc. Use a non-identifying case label; a facial model can itself identify a patient.

For a stalled capture, use **Share diagnostics** in the capture toolbar before restarting. You review and choose the destination in the system share sheet. The diagnostic report contains timing, readiness and processing state, without photographs, models, case labels or file paths. It is not sent automatically.

When cancelling, confirm **Discard capture** and wait for the unfinished capture to be removed. The capture screen stays open while camera/reconstruction writers stop and files are removed. If removal fails, unlock the iPhone, check available storage and retry using the capture screen. An error means the app has retained the unfinished files for cleanup; it does not mean they were deleted. Avoid deleting the app unless you have exported every saved scan you need.

Both modes reconstruct textured surfaces locally. Inspect coverage, holes, textures, orientation and known physical dimensions independently before using geometry in a CAD workflow. Photograph counts and capture progress do not establish accuracy. A face is particularly sensitive to motion and reflective eyes or teeth.

## Storage, export and deletion

Scans are saved in private, protected on-device storage. The app has no patient account, cloud reconstruction service or automatic upload. New photogrammetry captures remove source photographs and checkpoints after a completed model is validated. Saved models retain photographic textures and geometry that can identify a person. Older records from retired capture modes remain readable; any source data already associated with them remains local until deletion.

Open a saved scan, choose an available export format, and choose a destination in the share sheet. CAD mesh exports use millimetres. Legacy splat files, if present in an older record, remain exportable in metres for an external compatible viewer; the app no longer renders splats. Verify the receiving application’s units and anatomical left/right orientation. Formats do not enforce units.

Open a scan, choose **Scan actions → Delete scan**, and confirm to remove its saved model and capture data. Copies already exported to Files, other apps or recipients must be removed separately. Private scan storage is excluded from system backups; export the needed files before removing the app. The developer cannot recover locally lost scans.

If the app closes during saving, a completed local save may be restored automatically when the library opens after at least 24 hours. Recently modified, incomplete, damaged or conflicting saves are preserved rather than replacing an existing scan. If the library reports files it could not open, include the error wording and reproduction steps in a support request; do not email private scan files. This recovery cannot restore files removed from the device.

## Privacy

Read the in-app **Privacy and storage** view and the [privacy policy](PRIVACY_POLICY.md). Only public capture guides are exposed to Siri and Spotlight. Patient scans, case labels, images and geometry are excluded. Language resources are bundled; private scan content is never submitted to a translation service.
