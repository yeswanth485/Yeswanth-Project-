import codecs

def replace_html():
    with codecs.open('index.html', 'r', 'utf-8') as f:
        html = f.read()

    # Edit 1: Global Overlay
    old_overlay = '''            renderGlobalOverlays() {
                // Background status indicator
                let activeJob = null; // We could fetch /pipeline/status here
            },'''
    new_overlay = '''            renderGlobalOverlays() {
                if (pipelineState.paused && pipelineState.queueCount > 0 && !document.getElementById('pause-modal')) {
                    const modal = document.createElement('div');
                    modal.id = 'pause-modal';
                    modal.className = 'fixed inset-0 z-[300] bg-black/80 backdrop-blur-md flex items-center justify-center p-8 transition-opacity';
                    modal.innerHTML = `
                        <div class="glass max-w-lg w-full rounded-3xl border border-amber-500/30 shadow-2xl overflow-hidden animate-[pulse_2s_ease-in-out_infinite]">
                            <div class="p-8 border-b border-amber-500/10 bg-gradient-to-r from-amber-500/10 to-transparent">
                                <h3 class="text-2xl font-black text-amber-500 flex items-center gap-3"><i data-lucide="alert-triangle"></i> Automated Action Required</h3>
                            </div>
                            <div class="p-8 bg-black/80">
                                <p class="text-slate-300 text-sm mb-6 leading-relaxed">Vulnerabilities have been isolated and queued. The DevSecOps automation pipeline is currently paused pending security authorization.</p>
                                <div class="flex justify-end gap-4">
                                    <button onclick="document.getElementById('pause-modal').remove()" class="px-6 py-2 rounded-xl border border-white/10 text-slate-400 hover:text-white transition-all text-sm font-bold">Defer & View</button>
                                    <button onclick="document.getElementById('pause-modal').remove(); document.getElementById('pipeline-mini-status').innerText='STARTING ENGINE...'; pipelineState.startPipeline()" class="px-6 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-black font-black flex items-center gap-2 transition-all shadow-[0_0_20px_rgba(245,158,11,0.4)]">Authorize Remediation <i data-lucide="zap" class="w-4 h-4 text-black"></i></button>
                                </div>
                            </div>
                        </div>
                    `;
                    document.body.appendChild(modal);
                    if (window.lucide) window.lucide.createIcons();
                }
            },'''
    html = html.replace(old_overlay, new_overlay)

    # Edit 2: scanGithubRepo
    sig = '''            async startPipeline() {'''
    new_sig = '''            async scanGithubRepo(url) {
                if (!url || !url.includes('github.com/')) { alert('Please enter a valid GitHub repository URL.'); return; }
                console.log("[ACTION] GitHub Repo Scan:", url);
                try {
                    const res = await fetch(`${API_URL}/scan-github`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ url: url })
                    });
                    if (!res.ok) throw new Error(`HTTP ${res.status}`);
                    const data = await res.json();
                    this.currentScanId = data.scan_id;
                    this.scanStatus = 'RUNNING';
                    this.scanFinishedFlag = false;
                    app.terminalMode = 'scan';
                    router.go('terminal');
                    this.fetchTerminal();
                } catch (e) {
                    console.error("GitHub Scan Failed", e);
                    alert(`Failed to start GitHub scan: ${e.message}`);
                }
            },

            async startPipeline() {'''
    html = html.replace(sig, new_sig)

    # Edit 3: GitHub Analytics section string replace manually
    # Find updateWebsiteScannerDynamic block end
    scannerEnd = '''                        <div id="website-scanner-dynamic" data-render-hash="">
                            <!-- Dynamic Content -->
                        </div>
                    </div>
                </div>
            `;
            },'''
    new_scannerEnd = '''                        <div id="website-scanner-dynamic" data-render-hash="">
                            <!-- Dynamic Content -->
                        </div>
                    </div>
                </div>
                
                <!-- GitHub Scanner Input -->
                <div class="glass p-12 rounded-[45px] border border-blue-500/20 bg-[#0a0f18]/80 mt-12 mb-12 shadow-3xl relative overflow-hidden group">
                    <div class="absolute -top-32 -right-32 w-80 h-80 bg-blue-600/10 blur-[100px] rounded-full pointer-events-none group-hover:bg-blue-600/20 transition-colors"></div>
                    <div class="flex items-center gap-8 relative z-10">
                        <div class="w-24 h-24 rounded-3xl bg-blue-900/40 border border-blue-500/20 flex items-center justify-center shadow-inner">
                            <i data-lucide="github" class="w-12 h-12 text-blue-500"></i>
                        </div>
                        <div class="flex-1">
                            <h3 class="text-2xl font-black text-white mb-2 tracking-tight uppercase italic flex items-center gap-3">
                                GitHub Repository Analyzer 
                            </h3>
                            <p class="text-slate-500 text-sm font-medium max-w-2xl leading-relaxed">Supply a public GitHub repository URL to securely fetch and analyze the remote codebase for vulnerabilities.</p>
                        </div>
                    </div>
                    <div class="flex gap-6 mt-10 relative z-10">
                        <div class="flex-1 flex items-center bg-black/60 border border-white/5 rounded-3xl px-8 focus-within:border-blue-500/50 focus-within:ring-4 focus-within:ring-blue-500/5 transition-all shadow-inner group-hover:border-white/10">
                            <i data-lucide="github" class="w-6 h-6 text-slate-600 mr-4"></i>
                            <input type="url" id="github-url-input" placeholder="https://github.com/Username/Repository" class="bg-transparent text-lg font-mono text-white w-full py-6 outline-none">
                        </div>
                        <button onclick="pipelineState.scanGithubRepo(document.getElementById('github-url-input').value)" 
                            class="bg-gradient-to-br from-blue-700 to-indigo-800 hover:from-blue-600 hover:to-indigo-700 text-white font-black tracking-[0.3em] px-12 py-6 rounded-3xl shadow-[0_20px_40px_rgba(59,130,246,0.3)] hover:shadow-[0_25px_50px_rgba(59,130,246,0.5)] flex items-center gap-4 transition-all duration-500 shrink-0 hover:-translate-y-2 border border-blue-400/20">
                            <i data-lucide="search" class="w-5 h-5 text-blue-400"></i> SCAN REPO
                        </button>
                    </div>
                </div>
            `;
            },'''
    html = html.replace(scannerEnd, new_scannerEnd)

    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(html)
    print("Done")

if __name__ == "__main__":
    replace_html()
