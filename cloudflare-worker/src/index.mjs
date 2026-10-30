// Generated from tc_api_sdk/generated/api_schema.json in eladrave/tc-api-docs.
// This catalog is intentionally static and allowlisted. Never proxy arbitrary URLs.
const CATALOG = [
  {
    "name": "action_types_list_all_action_types",
    "title": "List all Action Types",
    "method": "GET",
    "path": "/api/action-types/"
  },
  {
    "name": "adhoccharges_list_all_ad_hoc_charges",
    "title": "List all Ad Hoc Charges",
    "method": "GET",
    "path": "/api/adhoccharges/"
  },
  {
    "name": "adhoccharges_get_an_ad_hoc_charge",
    "title": "Get an Ad Hoc Charge",
    "method": "GET",
    "path": "/api/adhoccharges/<id>/"
  },
  {
    "name": "adhoccharges_create_an_ad_hoc_charge",
    "title": "Create an Ad Hoc Charge",
    "method": "POST",
    "path": "/api/adhoccharges/"
  },
  {
    "name": "adhoccharges_update_an_ad_hoc_charge",
    "title": "Update an Ad Hoc Charge",
    "method": "PUT",
    "path": "/api/adhoccharges/<id>/"
  },
  {
    "name": "adhoccharges_delete_an_ad_hoc_charge",
    "title": "Delete an Ad Hoc Charge",
    "method": "DELETE",
    "path": "/api/adhoccharges/<id>/"
  },
  {
    "name": "ahc_categories_list_all_ahc_categories",
    "title": "List all Ad Hoc Charge Categories",
    "method": "GET",
    "path": "/api/ahc-categories/"
  },
  {
    "name": "agents_list_all_agents",
    "title": "List all Agents",
    "method": "GET",
    "path": "/api/agents/"
  },
  {
    "name": "agents_get_an_agent",
    "title": "Get an Agent",
    "method": "GET",
    "path": "/api/agents/<id>/"
  },
  {
    "name": "agents_create_an_agent",
    "title": "Create an Agent",
    "method": "POST",
    "path": "/api/agents/"
  },
  {
    "name": "agents_update_an_agent",
    "title": "Update an Agent",
    "method": "POST",
    "path": "/api/agents/"
  },
  {
    "name": "agents_label_add_to_an_agent",
    "title": "Add a Label to an Agent",
    "method": "POST",
    "path": "/api/agents/<id>/add_label/"
  },
  {
    "name": "agents_label_remove_from_an_agent",
    "title": "Removing a Label from an Agent",
    "method": "POST",
    "path": "/api/agents/<id>/add_label/"
  },
  {
    "name": "appointments_list_all_appointments",
    "title": "List all Appointments",
    "method": "GET",
    "path": "/api/appointments/"
  },
  {
    "name": "appointments_get_an_appointment",
    "title": "Get an Appointment",
    "method": "GET",
    "path": "/api/appointments/<id>/"
  },
  {
    "name": "appointments_create_an_appointment",
    "title": "Create an Appointment",
    "method": "POST",
    "path": "/api/appointments/"
  },
  {
    "name": "appointments_update_an_appointment",
    "title": "Update an Appointment",
    "method": "PUT",
    "path": "/api/appointments/<id>/"
  },
  {
    "name": "appointments_create_update_rcra",
    "title": "Add/Edit Recipient on Appointment",
    "method": "POST",
    "path": "/api/appointments/<id>/recipient/add/"
  },
  {
    "name": "appointments_remove_rcra",
    "title": "Remove Recipient from Appointment",
    "method": "POST",
    "path": "/api/appointments/<id>/recipient/remove/"
  },
  {
    "name": "appointments_create_update_cja",
    "title": "Add/Edit Contractor on Appointment",
    "method": "POST",
    "path": "/api/appointments/<id>/contractor/add/"
  },
  {
    "name": "appointments_remove_cja",
    "title": "Remove Contractor from Appointment",
    "method": "POST",
    "path": "/api/appointments/<id>/contractor/remove/"
  },
  {
    "name": "balance_updates_list_all_balance_updates",
    "title": "List all Balance Updates",
    "method": "GET",
    "path": "/api/balance_updates/"
  },
  {
    "name": "balance_updates_get_a_balance_update",
    "title": "Get a balance update",
    "method": "GET",
    "path": "/api/balance_updates/{id}/"
  },
  {
    "name": "balance_updates_create_a_balance_update",
    "title": "Create a balance update",
    "method": "POST",
    "path": "/api/balance_updates/"
  },
  {
    "name": "clients_list_all_clients",
    "title": "List all Clients",
    "method": "GET",
    "path": "/api/clients/"
  },
  {
    "name": "clients_get_a_client",
    "title": "Get a Client",
    "method": "GET",
    "path": "/api/clients/<id>/"
  },
  {
    "name": "clients_create_a_client",
    "title": "Create a Client",
    "method": "POST",
    "path": "/api/clients/"
  },
  {
    "name": "clients_update_a_client",
    "title": "Update a Client",
    "method": "POST",
    "path": "/api/clients/"
  },
  {
    "name": "clients_label_add_to_a_client",
    "title": "Add a Label to a Client",
    "method": "POST",
    "path": "/api/clients/<id>/add_label/"
  },
  {
    "name": "clients_label_remove_from_a_client",
    "title": "Removing a Label from a Client",
    "method": "POST",
    "path": "/api/clients/<id>/add_label/"
  },
  {
    "name": "contractors_list_all_contractors",
    "title": "List all Contractors",
    "method": "GET",
    "path": "/api/contractors/"
  },
  {
    "name": "contractors_get_a_contractor",
    "title": "Get a Contractor",
    "method": "GET",
    "path": "/api/contractors/<id>/"
  },
  {
    "name": "contractors_get_a_contractors_availability",
    "title": "Get a Contractor's Availability",
    "method": "GET",
    "path": "/api/contractor_availability/<id>/"
  },
  {
    "name": "contractors_create_a_contractor",
    "title": "Create a Contractor",
    "method": "POST",
    "path": "/api/contractors/"
  },
  {
    "name": "contractors_update_a_contractor",
    "title": "Update a Contractor",
    "method": "POST",
    "path": "/api/contractors/"
  },
  {
    "name": "contractors_label_add_to_a_contractor",
    "title": "Add a Label to a Contractor",
    "method": "POST",
    "path": "/api/contractors/<id>/add_label/"
  },
  {
    "name": "contractors_label_remove_from_a_contractor",
    "title": "Removing a Label from a Contractor",
    "method": "POST",
    "path": "/api/contractors/<id>/add_label/"
  },
  {
    "name": "contractor_skills_list_all_contractor_skills",
    "title": "List all Contractor Skills",
    "method": "GET",
    "path": "/api/contractor-skills/"
  },
  {
    "name": "contractor_skills_get_a_contractor_skill",
    "title": "Get a Contractor Skill",
    "method": "GET",
    "path": "/api/contractor-skills/<id>/"
  },
  {
    "name": "contractor_skills_create_a_contractor_skills",
    "title": "Create a Contractor Skill",
    "method": "POST",
    "path": "/api/contractor-skills/"
  },
  {
    "name": "contractor_skills_delete_a_contractor_skill",
    "title": "Delete a Contractor Skill",
    "method": "DELETE",
    "path": "/api/contractor-skills/<id>/"
  },
  {
    "name": "countries_list_all_countries",
    "title": "List all Countries",
    "method": "GET",
    "path": "/api/countries/"
  },
  {
    "name": "countries_get_a_country",
    "title": "Get a Country",
    "method": "GET",
    "path": "/api/countries/<id>/"
  },
  {
    "name": "enquiry_create_an_enquiry",
    "title": "Create an Enquiry",
    "method": "POST",
    "path": "/api/enquiry/"
  },
  {
    "name": "invoices_list_all_invoices",
    "title": "List all Invoices",
    "method": "GET",
    "path": "/api/invoices/"
  },
  {
    "name": "invoices_get_an_invoice",
    "title": "Get an Invoice",
    "method": "GET",
    "path": "/api/invoices/<id>/"
  },
  {
    "name": "invoices_take_invoice_payment",
    "title": "Take Invoice Payment",
    "method": "POST",
    "path": "/api/invoices/<id>/take_payment/"
  },
  {
    "name": "labels_list_all_labels",
    "title": "List all Labels",
    "method": "GET",
    "path": "/api/labels/"
  },
  {
    "name": "labels_get_a_label",
    "title": "Get a Label",
    "method": "GET",
    "path": "/api/labels/<id>/"
  },
  {
    "name": "note_list_all_notes",
    "title": "List all notes",
    "method": "GET",
    "path": "/api/notes/"
  },
  {
    "name": "note_get_a_note",
    "title": "Get a note",
    "method": "GET",
    "path": "/api/notes/<id>/"
  },
  {
    "name": "payment_orders_list_all_pos",
    "title": "List all Payment Orders",
    "method": "GET",
    "path": "/api/payment-orders/"
  },
  {
    "name": "payment_orders_get_an_po",
    "title": "Get an Payment Order",
    "method": "GET",
    "path": "/api/payment-orders/<id>/"
  },
  {
    "name": "payment_orders_take_po_payment",
    "title": "Take Payment Order Payment",
    "method": "POST",
    "path": "/api/payment-orders/<id>/take_payment/"
  },
  {
    "name": "pipeline_stages_list_pipeline_stages",
    "title": "List Pipeline Stages",
    "method": "GET",
    "path": "/api/pipeline-stages/"
  },
  {
    "name": "proforma_invoices_list_all_proforma_invoices",
    "title": "List all Proforma Invoices",
    "method": "GET",
    "path": "/api/proforma-invoices/"
  },
  {
    "name": "proforma_invoices_get_a_proforma_invoice",
    "title": "Get an Proforma Invoices",
    "method": "GET",
    "path": "/api/proforma-invoices/<id>/"
  },
  {
    "name": "proforma_invoices_create_a_pfi",
    "title": "Create a Proforma Invoices",
    "method": "POST",
    "path": "/api/proforma-invoices/"
  },
  {
    "name": "proforma_invoices_take_proforma_invoice_payment",
    "title": "Take Proforma Invoice Payment",
    "method": "POST",
    "path": "/api/proforma-invoices/<id>/take_payment/"
  },
  {
    "name": "public_contractors_list_all_public_contractors",
    "title": "List all Public Contractors",
    "method": "GET",
    "path": "/api/public_contractors/"
  },
  {
    "name": "public_contractors_get_a_public_contractor",
    "title": "Get a Public Contractor",
    "method": "GET",
    "path": "/api/public_contractors/<id>/"
  },
  {
    "name": "qual_level_list_all_qual_levels",
    "title": "List all Qualification Levels",
    "method": "GET",
    "path": "/api/qual_levels/"
  },
  {
    "name": "qual_level_get_a_qual_level",
    "title": "Get a Qualification Level",
    "method": "GET",
    "path": "/api/qual-levels/"
  },
  {
    "name": "qual_level_create_a_qual_level",
    "title": "Create a Qualification Level",
    "method": "POST",
    "path": "/api/qual-levels/"
  },
  {
    "name": "qual_level_delete_a_qual_level",
    "title": "Delete a Qualification Level",
    "method": "POST",
    "path": "/api/qual-levels/"
  },
  {
    "name": "recipients_list_all_recipients",
    "title": "List all Recipients",
    "method": "GET",
    "path": "/api/recipients/"
  },
  {
    "name": "recipients_get_a_recipient",
    "title": "Get a Recipient",
    "method": "GET",
    "path": "/api/recipients/<id>/"
  },
  {
    "name": "recipients_create_a_recipient",
    "title": "Create a Recipient",
    "method": "POST",
    "path": "/api/recipients/"
  },
  {
    "name": "recipients_update_a_recipient",
    "title": "Update a Recipient",
    "method": "POST",
    "path": "/api/recipients/"
  },
  {
    "name": "recipients_label_add_to_a_recipient",
    "title": "Add a Label to a Recipient",
    "method": "POST",
    "path": "/api/recipients/<id>/add_label/"
  },
  {
    "name": "recipients_label_remove_from_a_recipient",
    "title": "Removing a Label from a Recipient",
    "method": "POST",
    "path": "/api/recipients/<id>/add_label/"
  },
  {
    "name": "reports_list_all_reports",
    "title": "List all Reports",
    "method": "GET",
    "path": "/api/reports/"
  },
  {
    "name": "reports_get_a_report",
    "title": "Get a Report",
    "method": "GET",
    "path": "/api/reports/<id>/"
  },
  {
    "name": "reviews_list_all_reviews",
    "title": "List all Reviews",
    "method": "GET",
    "path": "/api/reviews/"
  },
  {
    "name": "wellbeing_concerns_list_all_wellbeing_concerns",
    "title": "List all Safeguarding/Wellbeing Concerns",
    "method": "GET",
    "path": "/api/wellbeing_concerns/"
  },
  {
    "name": "wellbeing_concerns_get_a_wellbeing_concern",
    "title": "Get a Safeguarding/Wellbeing Concern",
    "method": "GET",
    "path": "/api/wellbeing_concerns/<id>/"
  },
  {
    "name": "services_list_all_services",
    "title": "List all Services",
    "method": "GET",
    "path": "/api/services/"
  },
  {
    "name": "services_get_a_service",
    "title": "Get a Service",
    "method": "GET",
    "path": "/api/services/<id>/"
  },
  {
    "name": "services_create_a_service",
    "title": "Create a Service",
    "method": "POST",
    "path": "/api/services/"
  },
  {
    "name": "services_update_a_service",
    "title": "Update a Service",
    "method": "PUT",
    "path": "/api/services/<id>/"
  },
  {
    "name": "services_label_add_to_a_service",
    "title": "Add a Label to a Service",
    "method": "POST",
    "path": "/api/services/<id>/add_label/"
  },
  {
    "name": "services_label_remove_from_a_service",
    "title": "Removing a Label from a Service",
    "method": "POST",
    "path": "/api/services/<id>/remove_label/"
  },
  {
    "name": "services_create_update_cj",
    "title": "Add a Contractor to a Service",
    "method": "POST",
    "path": "/api/services/<id>/add/"
  },
  {
    "name": "services_remove_cj",
    "title": "Remove a Contractor from a Service",
    "method": "POST",
    "path": "/api/services/<id>/remove/"
  },
  {
    "name": "services_create_update_rcr",
    "title": "Add a Recipient to a Service",
    "method": "POST",
    "path": "/api/services/<id>/add/"
  },
  {
    "name": "services_remove_rcr",
    "title": "Remove a Recipient from a Service",
    "method": "POST",
    "path": "/api/services/<id>/remove/"
  },
  {
    "name": "subjects_list_all_subjects",
    "title": "List all Subjects",
    "method": "GET",
    "path": "/api/subjects/"
  },
  {
    "name": "subjects_get_a_subject",
    "title": "Get a Subject",
    "method": "GET",
    "path": "/api/subjects/"
  },
  {
    "name": "subjects_create_a_subject",
    "title": "Create a Subject",
    "method": "POST",
    "path": "/api/subjects/"
  },
  {
    "name": "subjects_delete_a_subject",
    "title": "Delete a Subject",
    "method": "POST",
    "path": "/api/subjects/"
  },
  {
    "name": "subject_categories_list_all_subject_categories",
    "title": "List all Subject Categories",
    "method": "GET",
    "path": "/api/subject-categories/"
  },
  {
    "name": "subject_categories_get_a_subject_category",
    "title": "Get a Subject Category",
    "method": "GET",
    "path": "/api/subject-categories/<id>/"
  },
  {
    "name": "tasks_list_all_tasks",
    "title": "List all Tasks",
    "method": "GET",
    "path": "/api/tasks/"
  },
  {
    "name": "tasks_get_a_task",
    "title": "Get a Task",
    "method": "GET",
    "path": "/api/tasks/<id>/"
  },
  {
    "name": "tenders_list_all_tenders",
    "title": "List all Tenders",
    "method": "GET",
    "path": "/api/tenders/"
  },
  {
    "name": "tenders_accept_a_tender",
    "title": "Accept a Tender",
    "method": "POST",
    "path": "/api/tenders/<id>/accept/"
  },
  {
    "name": "tenders_reject_a_tender",
    "title": "Reject a Tender",
    "method": "POST",
    "path": "/api/tenders/<id>/reject/"
  }
];

const TOOL_MAP = new Map(CATALOG.map((operation) => [operation.name, operation]));
const BASE_URL = "https://secure.tutorcruncher.com";
const SERVER = { name: "tutorcruncher-mcp-cloudflare", version: "1.0.0" };
const RESERVED_ARGUMENTS = new Set(["id", "params", "query", "payload", "json", "data", "model", "raw", "headers", "timeout"]);
const JSON_HEADERS = { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };

export function listTools() {
  return CATALOG.map((op) => ({
    name: op.name,
    description: op.title + "\n" + op.method + " " + op.path,
    inputSchema: {
      type: "object",
      properties: {
        id: { anyOf: [{ type: "integer" }, { type: "string" }], description: "Required for operations with <id> in their API path" },
        params: { type: "object", description: "TutorCruncher query parameters (filters, paging)" },
        payload: { description: "JSON request body for a create/update/action operation" },
        model: { type: "string", description: "Legacy Python SDK model name (accepted, ignored by this JSON-native Worker)" },
        raw: { type: "boolean", description: "Legacy SDK raw flag (accepted, responses are always JSON/text)" }
      },
      required: op.path.includes("<id>") ? ["id"] : [],
      additionalProperties: true
    }
  }));
}

function json(data, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(data), { status, headers: { ...JSON_HEADERS, ...extraHeaders } });
}
function rpcResult(id, result) {
  return { jsonrpc: "2.0", id, result };
}
function rpcError(id, code, message) {
  return { jsonrpc: "2.0", id, error: { code, message } };
}
function sanitizeKey(value) {
  return typeof value === "string" ? value.trim().replace(/^(?:bearer|token)\s+/i, "").trim() : "";
}
function getCredential(request, env) {
  const url = new URL(request.url);
  const authorization = sanitizeKey(request.headers.get("Authorization"));
  // Shared server credentials must ALWAYS be protected by a separate access token.
  if (env.MCP_ACCESS_TOKEN) {
    const presented = request.headers.get("X-MCP-Token") || authorization || url.searchParams.get("mcp_token") || "";
    if (presented !== env.MCP_ACCESS_TOKEN) return { status: 401, message: "Unauthorized MCP client" };
    const key = sanitizeKey(request.headers.get("X-TutorCruncher-API-Key") || env.TC_API_KEY);
    if (!key) return { status: 503, message: "TutorCruncher credentials are not configured" };
    return { key };
  }
  if (env.TC_API_KEY) {
    return { status: 503, message: "MCP_ACCESS_TOKEN must be configured before a shared TC_API_KEY can be used" };
  }
  // BYO TutorCruncher API token. Header is preferred; URL form is legacy compatibility.
  const key = sanitizeKey(request.headers.get("X-TutorCruncher-API-Key") || authorization || url.searchParams.get("TC_API_KEY"));
  return key ? { key } : { status: 401, message: "TutorCruncher API token required (Authorization: Bearer <token>)" };
}

function appendParams(url, params) {
  if (params === null || params === undefined) return;
  if (!params || typeof params !== "object" || Array.isArray(params)) throw Error("params must be an object");
  for (const [key, val] of Object.entries(params)) {
    if (val === undefined || val === null) continue;
    if (Array.isArray(val)) {
      for (const item of val) if (item !== null && item !== undefined) url.searchParams.append(key, String(item));
    } else if (typeof val === "object") {
      url.searchParams.append(key, JSON.stringify(val));
    } else {
      url.searchParams.append(key, String(val));
    }
  }
}

export async function callTutorCruncher(op, args, apiKey, fetchImpl = fetch) {
  if (!args || typeof args !== "object" || Array.isArray(args)) throw Error("Tool arguments must be a JSON object");
  let path = op.path;
  if (path.includes("<id>")) {
    const id = args.id;
    if ((typeof id !== "string" && typeof id !== "number") || String(id).length === 0) throw Error("id is required");
    path = path.replace("<id>", encodeURIComponent(String(id)));
  }
  if (!path.startsWith("/api/") || path.includes("://")) throw Error("Invalid operation path");
  const url = new URL(path, BASE_URL);
  const extras = Object.fromEntries(Object.entries(args).filter(([k]) => !RESERVED_ARGUMENTS.has(k)));
  const explicitParams = args.params ?? args.query;
  appendParams(url, explicitParams ?? (op.method === "GET" ? extras : null));
  const bodyValue = args.payload ?? args.json ?? args.data;
  const headers = { "Authorization": "token " + apiKey, "Accept": "application/json" };
  const init = { method: op.method, headers, signal: AbortSignal.timeout(30000) };
  if (bodyValue !== undefined && bodyValue !== null && op.method !== "GET") {
    init.body = JSON.stringify(bodyValue);
    headers["Content-Type"] = "application/json";
  }
  let upstream;
  try {
    upstream = await fetchImpl(url.toString(), init);
  } catch (error) {
    return { content: [{ type: "text", text: "TutorCruncher request failed: " + (error?.name === "TimeoutError" ? "timeout" : "network error") }], isError: true };
  }
  const body = await upstream.text();
  let parsed;
  try { parsed = body ? JSON.parse(body) : null; } catch { parsed = body; }
  if (!upstream.ok) {
    return { content: [{ type: "text", text: JSON.stringify({ status: upstream.status, error: parsed }) }], isError: true };
  }
  return { content: [{ type: "text", text: JSON.stringify(parsed) }] };
}

export async function handleRpc(msg, apiKey, fetchImpl = fetch) {
  if (!msg || typeof msg !== "object" || Array.isArray(msg) || msg.jsonrpc !== "2.0" || typeof msg.method !== "string") {
    return rpcError(msg?.id ?? null, -32600, "Invalid JSON-RPC request");
  }
  if (!Object.prototype.hasOwnProperty.call(msg, "id")) return null; // Notification; no JSON-RPC response.
  const id = msg.id;
  switch (msg.method) {
    case "initialize":
      return rpcResult(id, {
        protocolVersion: "2025-06-18",
        capabilities: { tools: { listChanged: false }, resources: { listChanged: false } },
        serverInfo: SERVER
      });
    case "ping":
      return rpcResult(id, {});
    case "tools/list":
      return rpcResult(id, { tools: listTools() });
    case "resources/list":
      return rpcResult(id, { resources: [{
        uri: "tutorcruncher://schema", name: "TutorCruncher Operation Catalog",
        description: "Method, resource, and path catalog generated from the original Python SDK schema",
        mimeType: "application/json"
      }] });
    case "resources/read":
      if (msg.params?.uri !== "tutorcruncher://schema") return rpcError(id, -32002, "Resource not found");
      return rpcResult(id, { contents: [{ uri: "tutorcruncher://schema", mimeType: "application/json", text: JSON.stringify(CATALOG) }] });
    case "tools/call": {
      const name = msg.params?.name;
      const op = TOOL_MAP.get(name);
      if (!op) return rpcError(id, -32602, "Unknown tool");
      try {
        const result = await callTutorCruncher(op, msg.params.arguments ?? {}, apiKey, fetchImpl);
        return rpcResult(id, result);
      } catch (error) {
        return rpcResult(id, { isError: true, content: [{ type: "text", text: "Tool error: " + (error?.message || "unknown") }] });
      }
    }
    default:
      return rpcError(id, -32601, "Method not found");
  }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/health" && request.method === "GET") {
      return json({ status: "ok", service: SERVER.name, tool_count: CATALOG.length, transport: "streamable-http", endpoint: "/mcp" });
    }
    if (url.pathname === "/" && request.method === "GET") {
      return json({ service: SERVER.name, endpoint: "/mcp", health: "/health" });
    }
    if (url.pathname !== "/mcp" && url.pathname !== "/sse") return json({ error: "Not found" }, 404);
    if (request.method !== "POST") {
      return json({ error: "Use POST /mcp with JSON-RPC Streamable HTTP; legacy SSE GET is not supported" }, 405, { Allow: "POST" });
    }
    const credential = getCredential(request, env);
    if (!credential.key) return json({ error: credential.message }, credential.status);
    if (!(request.headers.get("Content-Type") || "").toLowerCase().includes("application/json")) {
      return json({ error: "Content-Type must be application/json" }, 415);
    }
    let payload;
    try {
      const body = await request.text();
      if (body.length > 1048576) return json(rpcError(null, -32600, "Request too large"), 413);
      payload = JSON.parse(body);
    } catch {
      return json(rpcError(null, -32700, "Parse error"), 400);
    }
    try {
      if (Array.isArray(payload)) {
        if (!payload.length) return json(rpcError(null, -32600, "Empty batch"), 400);
        const responses = [];
        for (const message of payload) {
          const response = await handleRpc(message, credential.key);
          if (response) responses.push(response);
        }
        return responses.length ? json(responses) : new Response(null, { status: 202, headers: JSON_HEADERS });
      }
      const result = await handleRpc(payload, credential.key);
      return result ? json(result) : new Response(null, { status: 202, headers: JSON_HEADERS });
    } catch {
      return json(rpcError(null, -32603, "Internal error"), 500);
    }
  }
};
