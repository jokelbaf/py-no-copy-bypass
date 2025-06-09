# Py-No-Copy-Bypass

Quick and easy proxy to bypass copy protection on any website.

## Usage

1. Clone the repository and navigate to the directory:
```bash
git clone https://github.com/jokelbaf/py-no-copy-bypass.git
cd py-no-copy-bypass
```
2. Install the required dependencies:
```bash
uv sync
```
3. Run the proxy server:
```bash
uv run mitmproxy -p 8080 -s main.py
```

## Configuring machine to use the proxy

Before the bypass can work, you need to configure your machine to use the proxy server. I'm only going to cover the steps for Windows, but you can find similar instructions for other operating systems.

### Windows

1. Hit `Win` and type `Proxy settings`, then hit `Enter`.
2. In the `Manual proxy setup` section, click `Set up` on the `Use a proxy server` option.
3. Enter `localhost` as the address and `8080` as the port, toggle the `Use a proxy server` switch to `On`.
4. Click `Save` to apply the changes.
5. Open [mitm.it](http://mitm.it) in your browser and follow the instructions to install the CA certificate for your device.
7. Done! You can now visit any website and see that the copy protection has been bypassed.

## Testing the tool

You can visit [no-copy-demo.nekolab.app](https://no-copy-demo.nekolab.app) to test the tool. The website has a few copy protection mechanisms that the tool can bypass.
