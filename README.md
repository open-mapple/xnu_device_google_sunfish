# xnu_device_google_sunfish

The Google Pixel 4a (`sunfish`: Qualcomm SM7150 (Snapdragon 730G), 1080x2340) for Open Mapple: its configuration (`device.conf`, `configs/`).
Board facts (touch chip, pins, buses, panel) live here, not in the kernel.

**Build-only.** Nobody on the project owns this phone, so the kernel has been built for it but never run. Upstream's reports
are in the credited projects; a maintainer with the phone is welcome (see NOTICE for whose work this builds on).

Untested here: the GPU user interface (`sweetgpuabi=1`, an msm-style IOKit client over the Adreno 618 service: it compiles and links, nothing opens it yet), and the GPU page-table mode (`sweetgpuvm=1`: a 1 GiB window of scattered pages and 2,048 buffers instead of the contiguous 64 MiB one; compiles, never run).

Boot-args and ADT flags are in `device.conf`. The kernel is built from `xnu_kernel_qcom_common` with `config/MASTER.arm64.sweet`.

Licence: MIT (`LICENSE`); `NOTICE` credits the upstream authors; `LEGAL.md` says what never goes in.
