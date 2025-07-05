// SPDX-FileCopyrightText: (c) 2020 Silverlan <opensource@pragma-engine.com>
// SPDX-License-Identifier: MIT

#include <prosper_vulkan_definitions.hpp>
#include <pragma/engine.h>
#include <pragma/networkstate/networkstate.h>
#include <pragma/console/conout.h>
#include <sharedutils/util_library.hpp>
#include <vk_context.hpp>

#ifdef __linux__
#define DLLEXPORT __attribute__((visibility("default")))
#else
#define DLLEXPORT __declspec(dllexport)
#endif

static std::shared_ptr<util::Library> g_libNsightAftermath;
extern "C" {
DLLEXPORT bool initialize_render_api(const std::string &engineName, bool enableValidation, std::shared_ptr<prosper::IPrContext> &outContext, std::string &errMsg)
{
	outContext = prosper::VlkContext::Create(engineName, enableValidation);
	outContext->SetPreDeviceCreationCallback([](const prosper::util::VendorDeviceInfo &info) {
		if(info.vendor != prosper::Vendor::Nvidia) // Nsight Aftermath is only supported on Nvidia GPUs
			return;
		std::string err;
		auto lib = pragma::get_engine()->GetClientState()->LoadLibraryModule("nsight_aftermath/pr_nsight_aftermath", {}, &err);
		if(!lib) {
			Con::cwar << "Failed to load Nsight Aftermath: " << err << Con::endl;
			return;
		}
		auto *ptrAttachPragma = lib->FindSymbolAddress<bool (*)(std::string &)>("pragma_attach");
		if(!ptrAttachPragma) {
			Con::cwar << "Failed to find pragma_attach in Nsight Aftermath" << Con::endl;
			return;
		}
		if(ptrAttachPragma(err))
			g_libNsightAftermath = lib;
		else
			Con::cwar << "Failed to initialize Nsight Aftermath: " << err << Con::endl;
	});
	return true;
}
DLLEXPORT void pragma_detach()
{
	if(g_libNsightAftermath) {
		auto *detach = g_libNsightAftermath->FindSymbolAddress<void (*)()>("pragma_detach");
		if(detach)
			detach();
	}
	g_libNsightAftermath = {};
}
};
