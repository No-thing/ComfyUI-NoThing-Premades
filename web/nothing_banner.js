// No_Thing Banner: paints the banner picture as the whole node (no title bar, no body, no slots).
import { app } from "../../scripts/app.js";

const IMG = new Image();
let ready = false;
IMG.onload = () => { ready = true; if (app.graph) app.graph.setDirtyCanvas(true, true); };
IMG.src = new URL("./banners/workflow_banner.png", import.meta.url).href;

app.registerExtension({
  name: "NoThing.Banner",
  beforeRegisterNodeDef(nodeType, nodeData) {
    if (nodeData.name !== "NoThingBanner") return;
    const created = nodeType.prototype.onNodeCreated;
    nodeType.prototype.onNodeCreated = function () {
      created?.apply(this, arguments);
      this.size = [350, 820];                         // same ratio as the picture (620 x 1453)
      this.title = "";
      this.color = "#00000000"; this.bgcolor = "#00000000";
      this.flags = Object.assign(this.flags || {}, { collapsable: false });
      this.resizable = true;
      this.title_mode = (window.LiteGraph && window.LiteGraph.NO_TITLE) ?? 1;
      this.properties = this.properties || {};
    };
    nodeType.prototype.onDrawBackground = function (ctx) {
      if (!ready) return;
      const w = this.size[0], h = this.size[1];
      ctx.save();
      ctx.drawImage(IMG, 0, 0, w, h);
      ctx.restore();
    };
    nodeType.prototype.computeSize = function () { return this.size || [350, 820]; };
    // keep the picture's proportions when the user drags a corner
    const resized = nodeType.prototype.onResize;
    nodeType.prototype.onResize = function (size) {
      resized?.apply(this, arguments);
      size[1] = size[0] * 1453 / 620;
    };
  },
});
